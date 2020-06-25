import pandas as pd
from sklearn.model_selection import train_test_split

input_file = "./input/NewsAggregatorDataset/newsCorpora.csv"
news_corpora = pd.read_table(input_file, header=None)
news_corpora.columns = [
    "ID",
    "TITLE",
    "URL",
    "PUBLISHER",
    "CATEGORY",
    "STORY",
    "HOSTNAME",
    "TIMESTAMP"
]
news_corpora = news_corpora[news_corpora["PUBLISHER"].isin(
    ["Reuters", "Huffington Post", "Businessweek", "Contactmusic.com", "Daily Mail"]
)].sample(frac=1, random_state=0)

X = news_corpora[["TITLE", "CATEGORY"]].copy()
X["CATEGORY"] = X["CATEGORY"].map({
    "b": 0,
    "t": 1,
    "e": 2,
    "m": 3
})
y = X["CATEGORY"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=0)
X_valid, X_test, y_valid, y_test = train_test_split(X_test, y_test, test_size=0.5, stratify=y_test, random_state=0)

X_train.to_csv('./output/train.txt', sep='\t', index=False, header=None)
X_valid.to_csv('./output/valid.txt', sep='\t', index=False, header=None)
X_test.to_csv('./output/test.txt', sep='\t', index=False, header=None)
