import pandas as pd
from gensim.models import KeyedVectors
from tqdm import tqdm


def culculate_similarity(row):
    positive = [row["v2"], row["v3"]]
    negative = [row["v1"]]
    return pd.Series(list(model.most_similar(positive=positive, negative=negative))[0])


tqdm.pandas()
with open("./input/questions-words.txt") as rf:
    lines = rf.readlines()
lines = [line.rstrip("\n").split() for line in lines]

columns = ["category", "v1", "v2", "v3", "v4"]
datas = [[] for _ in range(5)]
for line in lines:
    if line[0] == ":":
        category = line[1]
        continue
    datas[0].append(category)
    for i in range(4):
        datas[i + 1].append(line[i])
df = pd.DataFrame(
    data={"category": datas[0], "v1": datas[1], "v2": datas[2], "v3": datas[3], "v4": datas[4]},
    columns=columns
)

model = KeyedVectors.load_word2vec_format('./input/GoogleNews-vectors-negative300.bin', binary=True)

df[["SimWord", "Score"]] = df.progress_apply(culculate_similarity, axis=1)
df.to_csv("./output/64.txt", sep=" ", index=False, header=None)
