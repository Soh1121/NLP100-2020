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


file_name = "./output/neko.txt.mecab"
with open(file_name) as rf:
    sentences = rf.read().split("EOS\n")

sentences = [parse(s) for s in sentences if len(parse(s)) != 0]

num_phrase_list = []
for sentence in sentences:
    num_phrase_list += num_connections(sentence)
print("\n".join(num_phrase_list))
