import pandas as pd

data_frame = pd.read_table("popular-names.txt", header=None)
data_frame_sort = data_frame[0].value_counts()
print(pd.Series(data_frame_sort.index.values, data_frame_sort.values))
