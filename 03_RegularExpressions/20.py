import pandas as pd

data_frame = pd.read_json("jawiki-country.json.gz", compression='infer', lines=True)
uk_text = data_frame.query('title == "イギリス"')['text'].values[0]
print(uk_text)
