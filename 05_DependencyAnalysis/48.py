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


def create_text(morphs):
    value = ""
    for morph in morphs:
        if morph.pos != "記号":
            value += morph.surface
    return value


def extraction_varb_base(morphs):
    for morph in morphs:
        if morph.pos == "動詞":
            return morph.base
    return False


def extraction_case(morphs):
    for i in morphs[::-1]:
        if i.pos == "記号":
            continue
        if i.pos == "助詞":
            return i.base
        return False


def find_function_verb(morphs):
    for index, morph in enumerate(morphs):
        if morph.pos1 != "サ変接続":
            continue
        if len(morphs) <= index + 1:
            continue
        if morphs[index + 1].surface != "を":
            continue
        return True
    return False


def find_verb_base(morphs):
    for morph in morphs:
        if morph.pos == "動詞":
            return morph


def has_noun(morphs):
    for morph in morphs:
        if morph.pos == "名詞":
            return True
    return False


def dependency(ans, dst, sentence):
    if dst == -1:
        return ans
    clause = sentence[dst]
    ans += " -> " + create_text(clause.morphs)
    dst = int(clause.dst.rstrip("D"))
    print(sentence[dst - 1].dst)
    return dependency(ans, dst, sentence)


file_name = "./output/neko.txt.cabocha"
with open(file_name) as rf:
    sentences = rf.read().split("EOS\n")
sentences = list(filter(lambda x: x != "", sentences))

result = []
for sentence in sentences:
    block = []
    chunk = parse(sentence)
    chunk_sorted = sorted(chunk.items(), key=lambda x: x[0])
    for i in chunk_sorted:
        block.append(Chunk(i[1]))
    result.append(block)

output = ""
for sentence in result:
    result = {}
    for clause in sentence:
        morphs = clause.morphs
        if not has_noun(morphs):
            continue
        dst = int(clause.dst.rstrip("D"))
        ans = create_text(morphs)
        print(dependency(ans, dst, sentence))

"""
file_name = "./output/47.txt"
with open(file_name, mode="w") as wf:
    wf.write(output)
"""
