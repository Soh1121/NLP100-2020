import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression


X_train = pd.read_table("./output/train.feature.txt", header=None)
y_train = pd.read_table("./output/train.txt", header=None)[1]

lr = LogisticRegression(penalty="l2", random_state=0, solver="sag", max_iter=10000)
lr.fit(X_train, y_train)
joblib.dump(lr, "./output/model.joblib", compress=True)
