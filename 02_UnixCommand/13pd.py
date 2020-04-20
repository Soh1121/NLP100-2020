import pandas as pd


c1 = pd.read_table("output/col1pd.txt", header=None)
c2 = pd.read_table("output/col2pd.txt", header=None)

data_frame = pd.concat([c1, c2], axis=1)
data_frame.to_csv("output/colspd.txt", sep='\t', index=False, header=None)
