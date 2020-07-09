import pandas as pd
from gensim.models import KeyedVectors
from tqdm import tqdm


def culculate_similarity(row):
    positive = [row["v2"], row["v3"]]
    negative = [row["v1"]]
    return pd.Series(list(model.most_similar(positive=positive, negative=negative))[0])


tqdm.pandas()
df = pd.read_csv("./input/questions-words.txt", sep=" ")
df = df.reset_index()
df.columns = ["v1", "v2", "v3", "v4"]
df = df.dropna()

model = KeyedVectors.load_word2vec_format('./input/GoogleNews-vectors-negative300.bin', binary=True)

df[["SimWord", "Score"]] = df.progress_apply(culculate_similarity, axis=1)
df.to_csv("./output/64.txt", sep=" ", index=False, header=None)
