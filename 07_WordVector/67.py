import pandas as pd
import numpy as np
from gensim.models import KeyedVectors
from sklearn.cluster import KMeans


CLUSTER_NUM = 5

# 国名データ：http://www.fao.org/countryprofiles/iso3list/en/
countries = pd.read_table("./input/countries.tsv")
countries = countries["Short name"]

model = KeyedVectors.load_word2vec_format(
    "./input/GoogleNews-vectors-negative300.bin", binary=True)

countries_vec = [model[country]
                 for country in countries
                 if country in model]

kmeans = KMeans(n_clusters=CLUSTER_NUM, random_state=0)
kmeans.fit(countries_vec)
for i in range(CLUSTER_NUM):
    cluster = np.where(kmeans.labels_ == i)[0]
    print("cluster:", i)
    print(", ".join([countries[j] for j in cluster]))
