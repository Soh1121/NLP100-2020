import joblib
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader
from torch import nn, optim


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


X_train = dataload("./output/X_train.joblib", "float")
X_valid = dataload("./output/X_valid.joblib", "float")
X_test = dataload("./output/X_test.joblib", "float")
y_train = dataload("./output/y_train.joblib", "int")
y_valid = dataload("./output/y_valid.joblib", "int")
y_test = dataload("./output/y_test.joblib", "int")

dataset_train = CreateDataset(X_train, y_train)
dataset_valid = CreateDataset(X_valid, y_valid)
dataset_test = CreateDataset(X_test, y_test)

dataloader_train = DataLoader(dataset_train, batch_size=1, shuffle=True)
dataloader_valid = DataLoader(dataset_valid, batch_size=len(dataset_valid), shuffle=False)
dataloader_test = DataLoader(dataset_test, batch_size=len(dataset_test), shuffle=False)

model = NN(X_train[0: 4].size()[1], 4)
cel = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

NUM_EPOCHS = 100
for epoch in range(NUM_EPOCHS):
    model.train()
    loss_train = 0.0
    for inputs, labels in dataloader_train:
        optimizer.zero_grad()

        outputs = model(inputs)
        loss = cel(outputs, labels)
        loss.backward()
        optimizer.step()

        loss_train += loss.item()
    loss_train /= len(dataloader_train)
    model.eval()
    with torch.no_grad():
        inputs, labels = next(iter(dataloader_valid))
        outputs = model(inputs)
        loss_valid = cel(outputs, labels)
