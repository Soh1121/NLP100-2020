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


def verb_surfaces(sentence):
    verbs = list(filter(lambda x: x["pos"] == "動詞", sentence))
    return [verb["surface"] for verb in verbs]


file_name = "./output/neko.txt.mecab"
with open(file_name) as rf:
    sentences = rf.read().split("EOS\n")

result = []
for sentence in sentences:
    if len(parse(sentence)) != 0:
        result.append(parse(sentence))

verb_surface_list = []
for sentence in result:
    # verb_surfaces += list(itertools.chain.from_iterable(verb_surfaces(sentence)))
    verb_surface_list += verb_surfaces(sentence)
print("\n".join(verb_surface_list))
