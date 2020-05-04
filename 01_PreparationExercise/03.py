pi = "Now I need a drink, \
      alcoholic of course, \
      after the heavy lectures \
      involving quantum mechanics."
table = str.maketrans('', '', ',.')
words = pi.translate(table).split()

print([len(i) for i in words])
