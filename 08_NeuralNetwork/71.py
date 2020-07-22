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
X_train = torch.from_numpy(X_train.astype(np.float32))
X = X_train[0: 4]

model = NN(X.size()[1], 4)
y_pred = torch.softmax(model(X), dim=-1)
print(y_pred)
