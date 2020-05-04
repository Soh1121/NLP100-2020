import sys
import pandas as pd


if len(sys.argv) != 2:
    print("Set a argument N, for example '$ python 15pd.py 3'.")
    sys.exit()

n = int(sys.argv[1])
data_frame = pd.read_table("popular-names.txt", header=None)

file_count = 0
i = 0
while i < len(data_frame):
    q, mod = divmod(file_count, 26)
    prefix = "./output/16/py_split_file_"
    suffix_1 = chr(ord('a') + q)
    suffix_2 = chr(ord('a') + mod)
    write_file = "{}{}{}".format(prefix, suffix_1, suffix_2)
    data_frame[i:i+n].to_csv(write_file, sep='\t', index=False, header=None)
    i += n
    file_count += 1
