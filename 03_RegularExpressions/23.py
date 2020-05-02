import pandas as pd
import re

data_frame = pd.read_json("jawiki-country.json.gz", compression='infer', lines=True)
uk_text = data_frame.query('title == "イギリス"')['text'].values[0]

pattern = r'^=(=*)(.+)=+$'
for line in uk_text.split("\n"):
    result = re.match(pattern, line)
    if result is None:
        continue
    print(result.group(2).strip('\s ='), len(result.group(1)))