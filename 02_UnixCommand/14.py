import sys


if len(sys.argv) != 2:
    print("Set an argument N, for example '$ python 14.py 3'.")
    sys.exit()

n = int(sys.argv[1])
file_name = "popular-names.txt"

with open(file_name) as rf:
    for i in range(n):
        print(rf.readline().rstrip())
