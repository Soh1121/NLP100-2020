import pandas as pd


data_frame = pd.read_table("popular-names.txt", header=None)
print(data_frame.sort_values(2, ascending=False))
