import pandas as pd
import re
import requests


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
    if result:
        return "".join(result.group(1, 2, 3))
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


def remove_footnote(value):
    pattern = r"(.*?)(<ref.*?</ref>)(.*)"
    result = re.match(pattern, value)
    if result:
        return "".join(result.group(1, 3))
    pattern = r"<ref.*/>"
    value = re.sub(pattern, "", value)
    return value


def remove_language(value):
    pattern = r"{{lang\|.*?\|(.*?)[}}|）]"
    result = re.match(pattern, value)
    if result:
        return result.group(1)
    return value


def remove_temporarylink(value):
    pattern = r"{{仮リンク\|.*\|(.*)}}"
    result = re.match(pattern, value)
    if result:
        return result.group(1)
    return value


def remove_zero(value):
    pattern = r"\{\{0\}\}"
    value = re.sub(pattern, "", value)
    return value


def remove_br(value):
    pattern = r"<br />"
    value = re.sub(pattern, "", value)
    return value


def remove_pipe(value):
    pattern = r".*\|(.*)"
    result = re.match(pattern, value)
    if result:
        return result.group(1)
    return value


file_name = "jawiki-country.json.gz"
data_frame = pd.read_json(file_name, compression='infer', lines=True)
uk_text = data_frame.query("title == 'イギリス'")['text'].values[0]

ans = basic_info_extraction(uk_text)
uk_data = {}
for key, value in ans.items():
    value = remove_footnote(value)
    value = remove_emphasis(value)
    value = remove_innerlink(value)
    value = remove_language(value)
    value = remove_temporarylink(value)
    value = remove_zero(value)
    value = remove_br(value)
    value = remove_pipe(value)
    uk_data[key] = value

S = requests.Session()
url = "https://en.wikipedia.org/w/api.php"
params = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "titles": "File:{}".format(uk_data["国旗画像"])
}

R = S.get(url=url, params=params)
data = R.json()

pages = data["query"]["pages"]
for k, v in pages.items():
    print(v['imageinfo'][0]['url'])
