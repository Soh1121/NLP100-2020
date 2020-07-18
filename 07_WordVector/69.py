import pandas as pd
import matplotlib.pyplot as plt
from gensim.models import KeyedVectors
from sklearn.manifold import TSNE


# 国名データ：http://www.fao.org/countryprofiles/iso3list/en/
countries = pd.read_table("./input/countries.tsv")
countries = countries["Short name"]

model = KeyedVectors.load_word2vec_format("./input/GoogleNews-vectors-negative300.bin", binary=True)

country_vecs = []
country_names = []
for country in countries:
    if country in model:
        country_vecs.append(model[country])
        country_names.append(country)

tsne = TSNE(random_state=0)
embedded = tsne.fit_transform(country_vecs)
plt.scatter(embedded[:, 0], embedded[:, 1])
for (x, y), name in zip(embedded, country_names):
    plt.annotate(name, (x, y))
plt.show()
