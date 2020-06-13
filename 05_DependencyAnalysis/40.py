class Morph():
    def __init__(self, surface, prop):
        self.surface = surface
        self.base = prop[6]
        self.pos = prop[0]
        self.pos1 = prop[1]


def parse(sentence):
    words = [i for i in sentence.split("\n") if i != ""]
    morphemes = []
    for word in words:
        if word[0] == "*":
            continue
        arg = word.split("\t")
        morphemes.append(Morph(arg[0], arg[1].split(",")))
    return morphemes


file_name = "./output/ai.ja.txt.cabocha"
with open(file_name) as rf:
    sentences = rf.read().split("EOS\n")
sentences = list(filter(lambda x: x != "", sentences))

result = []
for sentence in sentences:
    if len(parse(sentence)) != 0:
        result.append(parse(sentence))

for morpheme in result[2]:
    print(vars(morpheme))
