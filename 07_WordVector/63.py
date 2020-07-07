from gensim.models import KeyedVectors


model = KeyedVectors.load_word2vec_format('./input/GoogleNews-vectors-negative300.bin', binary=True)
print(model.most_similar(positive=['Spain', 'Athens'], negative=['Madrid'], topn=10))
