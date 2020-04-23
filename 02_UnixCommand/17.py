file_name = "popular-names.txt"
with open(file_name) as f:
    lines = f.readlines()
    item1 = list(map(lambda x: x.split()[0], lines))

item1 = list(set(item1))
item1.sort()
print("\n".join(item1))
