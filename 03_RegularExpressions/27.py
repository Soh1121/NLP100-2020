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


def remove_emphasis(value):
    pattern = r"(.*?)'{1,3}(.+?)'{1,3}(.*)"
    result = re.match(pattern, value)
    if result is not None:
        return "".join(result.group(1, 2, 3))
    else:
        return value


def remove_innerlink(value):
    pipe_pattern = r"(.*\[\[(.*?)\|(.+)\]\])"
    result = re.findall(pipe_pattern, value)
    if len(result) != 0:
        for i in result:
            pattern = "[[{}|{}]]".format(i[1], i[2])
            value = value.replace(pattern, i[2])
    pattern = r"(\[\[(.+?)\]\])"
    result = re.findall(pattern, value)
    if len(result) != 0:
        for i in result:
            if "[[ファイル:" not in value:
                value = value.replace(i[0], i[-1])
    return value


file_name = "jawiki-country.json.gz"
data_frame = pd.read_json(file_name, compression='infer', lines=True)
uk_text = data_frame.query("title == 'イギリス'")['text'].values[0]

ans = basic_info_extraction(uk_text)
for key, value in ans.items():
    value = remove_emphasis(value)
    value = remove_innerlink(value)
    print(key, ":", value)
