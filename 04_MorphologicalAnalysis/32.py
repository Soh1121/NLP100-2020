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


file_name = "./output/neko.txt.mecab"
with open(file_name) as rf:
    sentences = rf.read().split("EOS\n")

result = []
for sentence in sentences:
    if len(parse(sentence)) != 0:
        result.append(parse(sentence))

verb_base_list = []
for sentence in result:
    verb_base_list += verb_bases(sentence)
print("\n".join(verb_base_list))
