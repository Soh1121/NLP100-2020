import copy


class Morph():
    def __init__(self, surface, prop):
        self.surface = surface
        self.base = prop[6]
        self.pos = prop[0]
        self.pos1 = prop[1]

    def __repr__(self):
        ans = ""
        ans += "surface: " + self.surface
        ans += "\tbase: " + self.base
        ans += "\tpos: " + self.pos
        ans += "\tpos1: " + self.pos1
        return ans


class Chunk():
    def __init__(self, chunk):
        self.morphs = copy.copy(chunk["morphs"])
        self.dst = chunk["dst"]
        self.srcs = copy.copy(chunk["srcs"])


def parse(sentence):
    words = [i for i in sentence.split("\n") if i != ""]
    chunk = {}
    info = []
    for word in words:
        if word[0] == "*":
            info = word.split()
            if info[1] not in chunk:
                chunk[info[1]] = {
                    "morphs": [],
                    "srcs": []
                }
            chunk[info[1]]["dst"] = info[2]
            if info[2] == "-1D":
                continue
            if info[2][0] not in chunk:
                chunk[info[2][0]] = {
                    "morphs": [],
                    "srcs": [info[1]]
                }
            else:
                chunk[info[2][0]]["srcs"].append(info[1])
        else:
            arg = word.split("\t")
            chunk[info[1]]["morphs"].append(Morph(arg[0], arg[1].split(",")))
    return chunk


file_name = "./output/neko.txt.cabocha"
with open(file_name) as rf:
    sentences = rf.read().split("EOS\n")
sentences = list(filter(lambda x: x != "", sentences))

result = []
for sentence in sentences:
    chunk = parse(sentence)
    chunk_sorted = sorted(chunk.items(), key=lambda x: x[0])
    for i in chunk_sorted:
        result.append(Chunk(i[1]))

print(vars(result[7]))