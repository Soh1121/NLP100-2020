import sys
import pandas as pd


if len(sys.argv) != 2:
    print("Set a argument N, for example '$ python 14.py 3'.")
    sys.exit()

n = int(sys.argv[1])
data_frame = pd.read_table("popular-names.txt", header=None)
print(data_frame.head(n))
