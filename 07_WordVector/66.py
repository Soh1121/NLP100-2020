from tqdm import tqdm
from gensim.models import KeyedVectors
import pandas as pd


def culcSimScore(row):
    word1 = row["Word 1"]
    word2 = row["Word 2"]
    if word1 in model.wv and word2 in model.wv:
        score = model.wv.similarity(word1, word2)
    else:
        score = None
    return score


tqdm.pandas()
model = KeyedVectors.load_word2vec_format(
    './input/GoogleNews-vectors-negative300.bin', binary=True)
df = pd.read_csv("./input/wordsim353/combined.csv")
df["SimScore"] = df.progress_apply(culcSimScore, axis=1)

print(df[["Human (mean)", "SimScore"]].corr(method="spearman"))
