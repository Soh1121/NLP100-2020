import matplotlib.pyplot as plt
import japanize_matplotlib


def parse(sentence):
    morphemes = []
    words = sentence.split("\n")
    words = [i for i in words if i != ""]
    for word in words:
        result = {}
        morpheme = word.split("\t")
        info = morpheme[1].split(",")
        result = {
            "surface": morpheme[0],
            "base": info[6],
            "pos": info[0],
            "pos1": info[1]
        }
        morphemes.append(result)
    return morphemes


def verb_surfaces(sentence):
    verbs = list(filter(lambda x: x["pos"] == "動詞", sentence))
    return [verb["surface"] for verb in verbs]


def verb_bases(sentence):
    verbs = list(filter(lambda x: x["pos"] == "動詞", sentence))
    return [verb["base"] for verb in verbs]


def nouns_surfaces(sentence):
    nounses = list(filter(lambda x: x["pos"] == "名詞", sentence))
    return [nouns["surface"] for nouns in nounses]


def nouns_phrases(sentence):
    answer = []
    for i in range(len(sentence) - 2):
        words = sentence[i: i + 3]
        if words[1]["pos1"] == "連体化":
            answer.append("".join([j["surface"] for j in words]))
    return answer


def nouns_connections(sentence):
    answer = []
    nouns = []
    for word in sentence:
        if word["pos"] == "名詞":
            nouns.append(word["surface"])
        else:
            if 1 < len(nouns):
                answer.append("".join(nouns))
            nouns = []
    if 1 < len(nouns):
        answer.append("".join(nouns))
    return answer


def word_frequency_of_appearance(sentence, stopwords):
    frequency_of_appearance = {}
    target = nouns_surfaces(sentence)
    for word in target:
        if word in stopwords:
            continue
        if word not in frequency_of_appearance:
            frequency_of_appearance[word] = 1
        else:
            frequency_of_appearance[word] += 1
    return frequency_of_appearance


def cat_frequency_of_appearance(sentence, stopwords):
    frequency_of_appearance = {}
    target = nouns_surfaces(sentence)
    if "猫" in target:
        for word in target:
            if word in stopwords or word == "猫":
                continue
            if word not in frequency_of_appearance:
                frequency_of_appearance[word] = 1
            else:
                frequency_of_appearance[word] += 1
    return frequency_of_appearance


file_name = "./output/neko.txt.mecab"
with open(file_name) as rf:
    sentences = rf.read().split("EOS\n")

sentences = [parse(s) for s in sentences if len(parse(s)) != 0]

# ストップワードを設定
file_name = "./input/Japanese.txt"
with open(file_name) as rf:
    lines = rf.readlines()
stopwords = [i.rstrip() for i in lines]
stopwords += ["の", "ん", "——", "さ"]

# 名詞を対象に実施
frequency_of_appearance = {}
for sentence in sentences:
    new_frequency_of_appearance = cat_frequency_of_appearance(sentence, stopwords)
    for k, v in new_frequency_of_appearance.items():
        if k in frequency_of_appearance:
            frequency_of_appearance[k] += v
        else:
            frequency_of_appearance[k] = v

frequency_of_appearance_sorted = sorted(frequency_of_appearance.items(), key=lambda x: x[1], reverse=True)
top10 = frequency_of_appearance_sorted[:10]


labels = [ans[0] for ans in top10]
values = [ans[1] for ans in top10]
plt.figure(figsize=(8, 8))
plt.bar(labels, values)
plt.show()
