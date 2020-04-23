import pandas as pd
import numpy as np

data_frame = pd.read_table("popular-names.txt", header=None)
print("\n".join(np.sort(data_frame[0].unique())))
