import pandas as pd
import re


def basic_info_extraction(text):
    texts = text.split("\n")
    index = texts.index("{{基礎情報 国")
    basic_info = []
    for i in texts[index + 1:]:
        if i == "}}":
            break
        if i.find("|") != 0:
            basic_info[-1] += ", " + i
            continue
        basic_info.append(i)

    pattern = r"\|(.*)\s=(.*)"
    ans = {}
    for i in basic_info:
        result = re.match(pattern, i)
        ans[result.group(1)] = result.group(2).lstrip(" ")
    return ans


data_frame = pd.read_json("jawiki-country.json.gz", compression="infer", lines=True)
uk_text = data_frame.query("title == 'イギリス'")['text'].values[0]

ans = basic_info_extraction(uk_text)
for key, value in ans.items():
    print(key, ":", value)
