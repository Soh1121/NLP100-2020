import joblib
import torch
import numpy as np
import torch.nn as nn


class NN(nn.Module):
    def __init__(self, input_size, output_size):
        super().__init__()
        self.fc = nn.Linear(input_size, output_size, bias=False)
        nn.init.normal_(self.fc.weight, 0.0, 1.0)

    def forward(self, x):
        return self.fc(x)


X_train = joblib.load("./output/X_train.joblib")
y_train = joblib.load("./output/y_train.joblib")
X_train = torch.from_numpy(X_train.astype(np.float32))
y_train = torch.from_numpy(y_train)

model = NN(X_train[0: 4].size()[1], 4)
cel = nn.CrossEntropyLoss()
l_1 = cel(model(X_train[:1]), y_train[:1])
model.zero_grad()
l_1.backward()
print("【事例x_1】")
print("損失: {:.4f}".format(l_1))
print("勾配:")
print(model.fc.weight.grad, "\n")

l_4 = cel(model(X_train[:1]), y_train[:1])
model.zero_grad()
l_4.backward()
print("【事例x_4】")
print("損失: {:.4f}".format(l_4))
print("勾配:")
print(model.fc.weight.grad, "\n")
