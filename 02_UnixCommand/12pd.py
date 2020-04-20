import pandas as pd


data_frame = pd.read_table("popular-names.txt", header=None)
data_frame[0].to_csv("output/col1pd.txt", index=False, header=None)
data_frame[1].to_csv("output/col2pd.txt", index=False, header=None)
