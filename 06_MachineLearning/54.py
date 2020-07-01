import pandas as pd
import joblib
from sklearn.metrics import accuracy_score


X_train = pd.read_table("./output/train.feature.txt", header=None)
X_test = pd.read_table("./output/test.feature.txt", header=None)
y_train = pd.read_table("./output/train.txt", header=None)[1]
y_test = pd.read_table("./output/test.txt", header=None)[1]


lr = joblib.load("./output/model.joblib")
print(f"学習データ正解率：{accuracy_score(y_train, lr.predict(X_train)):.3f}")
print(f"評価データ正解率：{accuracy_score(y_test, lr.predict(X_test)):.3f}")
