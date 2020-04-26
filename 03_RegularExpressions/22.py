import pandas as pd
import re

data_frame = pd.read_json("jawiki-country.json.gz", compression='infer', lines=True)
uk_text = data_frame.query('title == "イギリス"')['text'].values[0]

pattern = r'\[\[Category:(.*)\]\]'
remove_pattern = r'\|.*'
for line in uk_text.split("\n"):
    result = re.match(pattern, line)
    if result is None:
        continue
    ans = re.sub(remove_pattern, '', result.group(1))
    print(ans)
