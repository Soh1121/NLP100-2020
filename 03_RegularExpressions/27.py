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
link_pattern = r"(\[\[(.*\|)*?(.+?)\]\])"
ans = {}
for i in basic_info:
    category_result = re.match(value_pattern, i)
    emphasis_result = re.match(emphasis_pattern, category_result.group(2).lstrip(" "))
    if emphasis_result is not None:
        value = emphasis_result.group(1) + emphasis_result.group(2) + emphasis_result.group(3)
        continue
    else:
        value = category_result.group(2).lstrip(" ")
    link_result = re.findall(link_pattern, value)
    if len(link_result) != 0:
        if "[[ファイル:" not in value:
            for i in link_result:
                value = value.replace(i[0], i[-1])
    ans[category_result.group(1)] = value
for key, value in ans.items():
    print(key, ":", value)
