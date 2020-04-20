import pandas as pd


file_name = "popular-names.txt"
data_frame = pd.read_table(file_name, header=None)
data_frame.to_csv("output/11pd_ans.txt", sep=" ", index=False, header=None)
