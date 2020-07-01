import pandas as pd
import joblib
import numpy as np
from sklearn.metrics import precision_score, recall_score, f1_score


def calculate_socres(y_true, y_pred):
    # 適合率
    precision = precision_score(y_true, y_pred, average=None)
    precision = np.append(precision, precision_score(y_true, y_pred, average='micro'))
    precision = np.append(precision, precision_score(y_true, y_pred, average='macro'))

    # 再現率
    recall = recall_score(y_true, y_pred, average=None)
    recall = np.append(recall, recall_score(y_true, y_pred, average='micro'))
    recall = np.append(recall, recall_score(y_true, y_pred, average='macro'))

    # F1スコア
    f1 = f1_score(y_true, y_pred, average=None)
    f1 = np.append(f1, f1_score(y_true, y_pred, average='micro'))
    f1 = np.append(f1, f1_score(y_true, y_pred, average='macro'))

    # 結果の結合
    scores = pd.DataFrame({"適合率": precision, "再現率": recall, "F1スコア": f1},
                          index=["b", "t", "e", "m", "マイクロ平均", "マクロ平均"])
    return scores


X_train = pd.read_table("./output/train.feature.txt", header=None)
X_test = pd.read_table("./output/test.feature.txt", header=None)
y_train = pd.read_table("./output/train.txt", header=None)
y_test = pd.read_table("./output/test.txt", header=None)

lr = joblib.load("./output/model.joblib")
y_pred = lr.predict(X_test)

print(calculate_socres(y_test[1], y_pred))
