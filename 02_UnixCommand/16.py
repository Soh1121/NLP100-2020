import sys


if len(sys.argv) != 2:
    print("Set an argument N, for exapmle '$ python 15.py 3'.")
    sys.exit()

n = int(sys.argv[1])
file_name = "popular-names.txt"

with open(file_name) as rf:
    lines = rf.readlines()

file_count = 0
i = 1
output = ""
for line in lines:
    output += line
    if i <= n - 1:
        i += 1
        continue
    q, mod = divmod(file_count, 26)
    prefix = "./output/16/py_split_file_"
    suffix_1 = chr(ord('a') + q)
    suffix_2 = chr(ord('a') + mod)
    write_file = "{}{}{}".format(prefix, suffix_1, suffix_2)
    with open(write_file, mode='w') as wf:
        wf.write(output)
    file_count += 1
    output = ""
    i = 1
