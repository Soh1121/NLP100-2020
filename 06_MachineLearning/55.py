import pandas as pd
import joblib
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt


X_train = pd.read_table("./output/train.feature.txt", header=None)
X_test = pd.read_table("./output/test.feature.txt", header=None)
y_train = pd.read_table("./output/train.txt", header=None)[1]
y_test = pd.read_table("./output/test.txt", header=None)[1]


lr = joblib.load("./output/model.joblib")
train_cm = confusion_matrix(y_train, lr.predict(X_train))
print(train_cm)
sns.heatmap(train_cm, annot=True, cmap='Blues')
plt.show()

test_cm = confusion_matrix(y_test, lr.predict(X_test))
print(test_cm)
sns.heatmap(test_cm, annot=True, cmap='Blues')
plt.show()
