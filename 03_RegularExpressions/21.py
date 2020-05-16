import pandas as pd
import re

file_name = "jawiki-country.json.gz"
data_frame = pd.read_json(file_name, compression='infer', lines=True)
uk_text = data_frame.query('title == "イギリス"')['text'].values[0]

pattern = r'\[\[Category:(.*)\]\]'
for line in uk_text.split("\n"):
    result = re.match(pattern, line)
    if result is not None:
        print(line)
