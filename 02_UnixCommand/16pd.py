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
    write_file = "./output/16/pd_split_file_" + chr(ord('a') + q) + chr(ord('a') + mod)
    data_frame[i:i+n].to_csv(write_file, sep='\t', index=False, header=None)
    i += n
    file_count += 1
