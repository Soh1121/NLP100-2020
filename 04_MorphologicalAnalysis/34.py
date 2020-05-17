def parse(sentence):
    morphemes = []
    words = sentence.split("\n")
    words = [i for i in words if i != ""]
    for word in words:
        result = {}
        result["surface"], info = extraction_surface(word)
        result["base"] = info[6]
        result["pos"] = info[0]
        result["pos1"] = info[1]
        morphemes.append(result)
    return morphemes


def extraction_surface(word):
    morpheme = word.split("\t")
    return morpheme[0], morpheme[1].split(",")


def verb_surfaces(sentences):
    answer = []
    for sentence in sentences:
        verbs = list(filter(lambda x: x["pos"] == "動詞", sentence))
        answer += [verb["surface"] for verb in verbs]
    return answer


def verb_bases(sentences):
    answer = []
    for sentence in sentences:
        verbs = list(filter(lambda x: x["pos"] == "動詞", sentence))
        answer += [verb["base"] for verb in verbs]
    return answer


def num_phrases(sentences):
    answer = []
    for sentence in sentences:
        for i in range(len(sentence)):
            words = sentence[i: i + 3]
            if len(words) != 3:
                break
            if words[1]["pos1"] == "連体化":
                answer.append("".join([j["surface"] for j in words]))
    return answer


def num_connections(sentences):
    answer = []
    for sentence in sentences:
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

result = []
for sentence in sentences:
    if len(parse(sentence)) != 0:
        result.append(parse(sentence))

num_connections = num_connections(result)
print("\n".join(num_connections))
