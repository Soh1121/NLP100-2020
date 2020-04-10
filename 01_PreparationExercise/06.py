def n_gram(target, n):
    return [target[index: index + n] for index in range(len(target) - n + 1)]

word1 = "paraparaparadise"
word2 = "paragraph"
x = set(n_gram(word1, 2))
y = set(n_gram(word2, 2))

# 和集合
print(x | y)
# 積集合
print(x & y)
# 差集合
print(x - y)
print(y - x)

print('se' in x)
print('se' in y)
