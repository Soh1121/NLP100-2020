pi = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
table = str.maketrans('', '', ',.')
words = pi.translate(table).split()

chars_num = []
for i in words:
    chars_num.append(len(i))
print(chars_num)
