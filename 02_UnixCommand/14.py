n = int(input())
file_name = "popular-names.txt"

with open(file_name) as rf:
    lines = rf.readlines()

for i in range(n):
    print("".join(lines[i].rstrip()))
