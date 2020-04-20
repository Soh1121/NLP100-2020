import pandas as pd


file_name = "popular-names.txt"
data_frame = pd.read_table(file_name, header=None)
print(len(data_frame))
