import pandas as pd
import matplotlib.pyplot as plt
from gensim.models import KeyedVectors
from scipy.cluster.hierarchy import linkage, dendrogram


# 国名データ：http://www.fao.org/countryprofiles/iso3list/en/
countries = pd.read_table("./input/countries.tsv")
countries = countries["Short name"]

model = KeyedVectors.load_word2vec_format(
    "./input/GoogleNews-vectors-negative300.bin", binary=True)

country_vecs = []
country_names = []
for country in countries:
    if country in model:
        country_vecs.append(model[country])
        country_names.append(country)

X = linkage(country_vecs, method="ward", metric="euclidean")
plt.figure(num=None, figsize=(15, 5), dpi=200, facecolor="w", edgecolor="k")
dendrogram(X, labels=country_names)
plt.show()
