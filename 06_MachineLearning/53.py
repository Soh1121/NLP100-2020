import pandas as pd
import numpy as np
import joblib


def score_lr(lr, X):
    return [np.max(lr.predict_proba(X), axis=1), lr.predict(X)]


X_train = pd.read_table("./output/train.feature.txt", header=None)
with open("./output/model.joblib", mode="rb") as f:
    lr = joblib.load(f)
train_pred = score_lr(lr, X_train)
print(train_pred)
