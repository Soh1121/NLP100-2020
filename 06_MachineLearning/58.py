import numpy as np
import pandas as pd
from tqdm import tqdm
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


X_train = pd.read_table("./output/train.feature.txt", header=None)
X_valid = pd.read_table("./output/valid.feature.txt", header=None)
X_test = pd.read_table("./output/test.feature.txt", header=None)
y_train = pd.read_table("./output/train.txt", header=None)[1]
y_valid = pd.read_table("./output/valid.txt", header=None)[1]
y_test = pd.read_table("./output/test.txt", header=None)[1]

result = []
for C in tqdm(np.logspace(-5, 4, 10)):
    lr = LogisticRegression(penalty="l2", random_state=0, solver="sag", C=C, max_iter=10000)
    lr.fit(X_train, y_train)
    train_pred = lr.predict(X_train)
    valid_pred = lr.predict(X_valid)
    test_pred = lr.predict(X_test)

    train_acc = accuracy_score(y_train, train_pred)
    valid_acc = accuracy_score(y_valid, valid_pred)
    test_acc = accuracy_score(y_test, test_pred)
    result.append([C, train_acc, valid_acc, test_acc])

result = np.array(result).T
plt.plot(result[0], result[1], label="train")
plt.plot(result[0], result[2], label="valid")
plt.plot(result[0], result[3], label="test")
plt.ylim(0, 1.1)
plt.ylabel("Accuracy")
plt.xscale("log")
plt.xlabel("C")
plt.legend()
plt.show()
