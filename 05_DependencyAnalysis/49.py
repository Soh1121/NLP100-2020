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


def create_convert_text(morphs, convert_char):
    value = ""
    flag = 0
    for morph in morphs:
        if morph.pos == "記号":
            continue
        if morph.pos == "名詞" and flag == 0:
            value += convert_char
            flag = 1
            continue
        if morph.pos == "名詞" and flag == 1:
            continue
        if morph.pos != "名詞" and flag == 1:
            flag = 2
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
    morphs = clause.morphs
    ans += " -> " + create_text(morphs)
    dst = clause.dst
    if not has_noun(morphs):
        return ans
    return dependency(ans, dst, sentence)


def create_dst_lists(dst, dst_lists, sentence):
    dst_lists.append(dst)
    if dst < 0:
        return dst_lists
    this_dst = sentence[dst].dst
    return create_dst_lists(this_dst, dst_lists, sentence)


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
for sentence in [result[33]]:
    result = {}
    nouns_phrases = []
    # 名詞句を抽出してリスト化
    for clause in sentence:
        morphs = clause.morphs
        if has_noun(morphs):
            nouns_phrases.append(clause)
    for i, clause in enumerate(sentence):
        if clause not in nouns_phrases:
            continue
        x_dst_lists = create_dst_lists(clause.dst, [], sentence)
        for j in range(len(nouns_phrases)):
            if i == j:
                continue
            # 文節iから構文木の根に至る経路上に文節jが存在する場合: 文節iから文節jのパスを表示
            if j in x_dst_lists:
                words = [create_convert_text(clause.morphs, "X")]
                for c in x_dst_lists[:x_dst_lists.index(j) + 1]:
                    if c == j:
                        words.append(create_convert_text(sentence[c].morphs, "Y"))
                    else:
                        words.append(create_text(sentence[c].morphs))
                print(" -> ".join(words))
                continue

file_name = "./output/49.txt"
with open(file_name, mode="w") as wf:
    wf.write(output)
