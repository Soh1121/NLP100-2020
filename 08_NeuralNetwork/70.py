import pandas as pd
import numpy as np
import joblib
from tqdm import tqdm
from gensim.models import KeyedVectors


def culcFeatureVec(row):
    emb = [model[word] if word in model.vocab else np.zeros(
        shape=(model.vector_size,))for word in row["TITLE"].split()]
    emb = np.mean(np.array(emb), axis=0)
    return emb


X_train = pd.read_table("../06_MachineLearning/output/train.txt", header=None)
X_valid = pd.read_table("../06_MachineLearning/output/valid.txt", header=None)
X_test = pd.read_table("../06_MachineLearning/output/test.txt", header=None)
cols = ["TITLE", "CATEGORY"]
X_train.columns = cols
X_valid.columns = cols
X_test.columns = cols
print("【学習データ】")
print(X_train["CATEGORY"].value_counts())
print("【検証データ】")
print(X_valid["CATEGORY"].value_counts())
print("【評価データ】")
print(X_test["CATEGORY"].value_counts())

data = pd.concat([X_train, X_valid, X_test]).reset_index(drop=True)

tqdm.pandas()
model = KeyedVectors.load_word2vec_format(
    "../07_WordVector//input/GoogleNews-vectors-negative300.bin", binary=True)
feature_vector = data.progress_apply(culcFeatureVec, axis=1)

X_train = np.array(list(feature_vector.values)[:len(X_train)])
X_valid = np.array(
    list(
        feature_vector.values)[
            len(X_train):len(X_train) +
        len(X_valid)])
X_test = np.array(list(feature_vector.values)[len(X_train) + len(X_valid):])
joblib.dump(X_train, "./output/X_train.joblib")
joblib.dump(X_valid, "./output/X_valid.joblib")
joblib.dump(X_test, "./output/X_test.joblib")

y_data = data["CATEGORY"]
y_train = y_data.values[:len(X_train)]
y_valid = y_data.values[len(X_train):len(X_train) + len(X_valid)]
y_test = y_data.values[len(X_train) + len(X_valid):]
joblib.dump(y_train, "./output/y_train.joblib")
joblib.dump(y_valid, "./output/y_valid.joblib")
joblib.dump(y_test, "./output/y_test.joblib")
