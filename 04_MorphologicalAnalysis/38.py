import matplotlib.pyplot as plt
from collections import defaultdict


def parse(sentence):
    morphemes = []
    words = sentence.split("\n")
    words = [i for i in words if i != ""]
    for word in words:
        result = {}
        morpheme = word.split("\t")
        result["surface"] = morpheme[0]
        info = morpheme[1].split(",")
        result["base"] = info[6]
        result["pos"] = info[0]
        result["pos1"] = info[1]
        morphemes.append(result)
    return morphemes


def verb_surfaces(sentence):
    verbs = list(filter(lambda x: x["pos"] == "動詞", sentence))
    return [verb["surface"] for verb in verbs]


def verb_bases(sentence):
    verbs = list(filter(lambda x: x["pos"] == "動詞", sentence))
    return [verb["base"] for verb in verbs]


def num_surfaces(sentence):
    nums = list(filter(lambda x: x["pos"] == "名詞", sentence))
    return [num["surface"] for num in nums]


def num_phrases(sentence):
    answer = []
    for i in range(len(sentence)):
        words = sentence[i: i + 3]
        if len(words) != 3:
            break
        if words[1]["pos1"] == "連体化":
            answer.append("".join([j["surface"] for j in words]))
    return answer


def num_connections(sentence):
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
    target = num_surfaces(sentence)
    for word in target:
        if word in stopwords:
            continue
        if word not in frequency_of_appearance:
            frequency_of_appearance[word] = 1
        else:
            frequency_of_appearance[word] += 1
    return frequency_of_appearance


file_name = "./output/neko.txt.mecab"
with open(file_name) as rf:
    sentences = rf.read().split("EOS\n")

result = []
for sentence in sentences:
    if len(parse(sentence)) != 0:
        result.append(parse(sentence))

# ストップワードを設定
file_name = "./input/Japanese.txt"
with open(file_name) as rf:
    lines = rf.readlines()
stopwords = [i.rstrip() for i in lines]
stopwords += ["の", "ん", "——", "さ", "ろ"]

# 名詞を対象に実施
frequency_of_appearance = {}
for sentence in result:
    new_frequency_of_appearance = word_frequency_of_appearance(sentence, stopwords)
    for k, v in new_frequency_of_appearance.items():
        if k in frequency_of_appearance:
            frequency_of_appearance[k] += v
        else:
            frequency_of_appearance[k] = v

word_frequency_of_appearance_hist = defaultdict(int)
for v in frequency_of_appearance.values():
    word_frequency_of_appearance_hist[v] += 1

ans = word_frequency_of_appearance_hist.values()
plt.figure(figsize=(8, 8))
plt.hist(ans, bins=100)
plt.show()
