def n_gram(target, n):
    return [target[index: index + n] for index in range(len(target) - n + 1)]

words = "I am an NLPer"
print(n_gram(words.split(), 2))
print(n_gram(words, 2))
