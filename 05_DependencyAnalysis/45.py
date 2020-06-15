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
            sentence_number = int(info[1])
            if sentence_number not in chunk:
                chunk[sentence_number] = {
                    "morphs": [],
                    "srcs": []
                }
            contact_number = int(info[2].rstrip("D"))
            chunk[sentence_number]["dst"] = contact_number
            if info[2] == "-1D":
                continue
            if contact_number not in chunk:
                chunk[contact_number] = {
                    "morphs": [],
                    "srcs": [sentence_number]
                }
            else:
                chunk[contact_number]["srcs"].append(sentence_number)
        else:
            arg = word.split("\t")
            chunk[sentence_number]["morphs"].append(Morph(arg[0], arg[1].split(",")))
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


file_name = "./output/ai.ja.txt.cabocha"
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
        case = extraction_case(morphs)
        if not case:
            continue
        if morphs[-1].pos == "助詞" and clause.dst != -1:
            to_clause = sentence[clause.dst]
            to_morphs = to_clause.morphs
            if "動詞" in [j.pos for j in to_morphs]:
                verb = extraction_varb_base(to_morphs)
                if verb:
                    if verb in result:
                        result[verb].add(case)
                    else:
                        result[verb] = set(case)
    for k, v in result.items():
        output += k + "\t" + " ".join(list(v)) + "\n"

file_name = "./output/45.txt"
with open(file_name, mode="w") as wf:
    wf.write(output)
