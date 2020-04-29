import pandas as pd
import re

data_frame = pd.read_json("jawiki-country.json.gz", compression="infer", lines=True)
uk_text = data_frame.query("title == 'イギリス'")['text'].values[0]

uk_texts = uk_text.split("\n")
index = uk_texts.index("{{基礎情報 国")
basic_info = []
for i in uk_texts[index + 1:]:
    if i == "}}":
        break
    if i.find("|") != 0:
        basic_info[-1] += ", " + i
        continue
    basic_info.append(i)

value_pattern = r"\|(.*)\s=(.*)"
emphasis_pattern = r"(.*?)'{1,3}(.+?)'{1,3}(.*)"
ans = {}
for i in basic_info:
    result = re.match(value_pattern, i)
    emphasis_result = re.match(emphasis_pattern, result.group(2).lstrip(" "))
    if emphasis_result is not None:
        ans[result.group(1)] = emphasis_result.group(1) + emphasis_result.group(2) + emphasis_result.group(3)
        continue
    ans[result.group(1)] = result.group(2).lstrip(" ")
for key, value in ans.items():
    print(key, ":", value)
