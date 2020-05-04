import pandas as pd

file_name = "jawiki-country.json.gz"
data_frame = pd.read_json(file_name, compression='infer', lines=True)
uk_text = data_frame.query('title == "イギリス"')['text'].values[0]
print(uk_text)
