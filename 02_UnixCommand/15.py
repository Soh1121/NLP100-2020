import sys


if len(sys.argv) != 2:
    print("Set an argument N, for exapmle '$ python 15.py 3'.")
    sys.exit()

n = int(sys.argv[1])
file_name = "popular-names.txt"

with open(file_name) as rf:
    lines = rf.readlines()

for i in lines[len(lines) - n:len(lines)]:
    print("".join(i.rstrip()))
