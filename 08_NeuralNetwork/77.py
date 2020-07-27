import joblib
import numpy as np
import torch
import time
from torch.utils.data import Dataset, DataLoader
from torch import nn, optim
from matplotlib import pyplot as plt


class NN(nn.Module):
    def __init__(self, input_size, output_size):
        super().__init__()
        self.fc = nn.Linear(input_size, output_size, bias=False)
        nn.init.normal_(self.fc.weight, 0.0, 1.0)

    def forward(self, x):
        return self.fc(x)


class CreateDataset(Dataset):
    def __init__(self, X, y):
        self.X = X
        self.y = y

    def __len__(self):
        return len(self.y)

    def __getitem__(self, index):
        return [self.X[index], self.y[index]]


def dataload(file_name, type_name):
    data = joblib.load(file_name)
    if type_name == "float":
        data = torch.from_numpy(data.astype(np.float32))
    elif type_name == "int":
        data = torch.from_numpy(data.astype(np.int64))
    return data


def calculate_loss_accuracy(model, cel, loader):
    model.eval()
    loss = 0.0
    total = 0
    correct = 0
    with torch.no_grad():
        for inputs, labels in loader:
            outputs = model(inputs)
            loss += cel(outputs, labels).item()
            pred = torch.argmax(outputs, dim=-1)
            total += len(inputs)
            correct += (pred == labels).sum().item()
    return loss / len(loader), correct / total


def model_train(
        dataset_train,
        dataset_valid,
        batch_size,
        model,
        criterion,
        optimizer,
        num_epochs):
    dataloader_train = DataLoader(
        dataset_train,
        batch_size=batch_size,
        shuffle=True)
    dataloader_valid = DataLoader(
        dataset_valid,
        batch_size=len(dataset_valid),
        shuffle=False)

    train_losses = []
    valid_losses = []
    train_accs = []
    valid_accs = []
    for epoch in range(num_epochs):
        start_time = time.time()

        model.train()
        for inputs, labels in dataloader_train:
            optimizer.zero_grad()

            outputs = model(inputs)
            loss = cel(outputs, labels)
            loss.backward()
            optimizer.step()
        loss_train, acc_train = calculate_loss_accuracy(
            model, cel, dataloader_train)
        loss_valid, acc_valid = calculate_loss_accuracy(
            model, cel, dataloader_valid)
        train_losses.append(loss_train)
        valid_losses.append(loss_valid)
        train_accs.append(acc_train)
        valid_accs.append(acc_valid)
        torch.save({
            'epoch': epoch,
            'model_state_dict': model.state_dict(),
            'optimizer_state_dict': optimizer.state_dict()
        },
            "./output/77/checkpoint{}.pt".format(epoch + 1))
        print(
            "epoch: {}, loss_train: {:.4f}, accuracy_train: {:.4f}, loss_valid: {:.4f}, accuracy_valid: {:.4f}".format(
                epoch +
                1,
                loss_train,
                acc_train,
                loss_valid,
                acc_valid))
    return {
        "train_losses": train_losses,
        "valid_losses": valid_losses,
        "train_accs": train_accs,
        "valid_accs": valid_accs
    }


X_train = dataload("./output/X_train.joblib", "float")
X_valid = dataload("./output/X_valid.joblib", "float")
y_train = dataload("./output/y_train.joblib", "int")
y_valid = dataload("./output/y_valid.joblib", "int")

dataset_train = CreateDataset(X_train, y_train)
dataset_valid = CreateDataset(X_valid, y_valid)

model = NN(X_train[0: 4].size()[1], 4)
cel = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

NUM_EPOCHS = 100

plt.plot(train_losses, label="train loss")
plt.plot(valid_losses, label="valid loss")
plt.legend()
plt.show()

plt.plot(train_accs, label="train acc")
plt.plot(valid_accs, label="valid acc")
plt.legend()
plt.show()
