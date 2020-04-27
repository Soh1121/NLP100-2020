import pandas as pd
import re

data_frame = pd.read_json("jawiki-country.json.gz", compression='infer', lines=True)
uk_text = data_frame.query('title == "イギリス"')['text'].values[0]

pattern = r'ファイル:(.+?)\|(thumb\|.*)+?'
for line in uk_text.split("\n"):
    result = re.finditer(pattern, line)
    if result is None:
        continue
    for match in result:
        print(match.group(1))
