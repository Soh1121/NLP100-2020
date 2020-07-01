# 出現頻度を標準化した値を特徴量とする
import string
import re
import pandas as pd
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import StandardScaler


def preprocessing(text):
    table = str.maketrans(string.punctuation, " " * len(string.punctuation))
    text = text.translate(table)        # 記号をスペースに変換
    text = text.lower()                 # 大文字→小文字に変換
    text = re.sub("[0-9]+", "0", text)  # 数字列をゼロに置換
    return text


X_train = pd.read_table("./output/train.txt", header=None)
X_valid = pd.read_table("./output/valid.txt", header=None)
X_test = pd.read_table("./output/test.txt", header=None)
cols = ["TITLE", "CATEGOLY"]
X_train.columns = cols
X_valid.columns = cols
X_test.columns = cols
X_train["LABEL"] = "train"
X_valid["LABEL"] = "valid"
X_test["LABEL"] = "test"

df = pd.concat([X_train, X_valid, X_test]).reset_index(drop=True)
df["TITLE"] = df["TITLE"].map(lambda x: preprocessing(x))
vectorizer = CountVectorizer()
bag = vectorizer.fit_transform(df["TITLE"])
scaler = StandardScaler()
df_std = scaler.fit_transform(bag.toarray())
df = pd.concat([df, pd.DataFrame(df_std)], axis=1)

# 57.pyで利用
joblib.dump(vectorizer.vocabulary_, "./output/vocabulary_.joblib")

X_train = df.query("LABEL == 'train'").drop(cols + ["LABEL"], axis=1)
X_valid = df.query("LABEL == 'valid'").drop(cols + ["LABEL"], axis=1)
X_test = df.query("LABEL == 'test'").drop(cols + ["LABEL"], axis=1)

X_train.to_csv("./output/train.feature.txt", sep="\t", index=False, header=None)
X_valid.to_csv("./output/valid.feature.txt", sep="\t", index=False, header=None)
X_test.to_csv("./output/test.feature.txt", sep="\t", index=False, header=None)
