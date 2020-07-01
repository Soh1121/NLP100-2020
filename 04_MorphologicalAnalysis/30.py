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


file_name = "./output/neko.txt.mecab"
with open(file_name) as rf:
    sentences = rf.read().split("EOS\n")

sentences = [parse(s) for s in sentences if len(parse(s)) != 0]
print(sentences)
