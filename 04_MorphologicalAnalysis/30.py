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


file_name = "./output/neko.txt.mecab"
with open(file_name) as rf:
    sentences = rf.read().split("EOS\n")

print(sentences)
result = []
for sentence in sentences:
    result.append(parse(sentence))
print(result)
