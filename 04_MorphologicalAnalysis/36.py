import matplotlib.pyplot as plt
import japanize_matplotlib


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

result = []
for sentence in sentences:
    if len(parse(sentence)) != 0:
        result.append(parse(sentence))

answer = {}
for sentence in result:
    for morpheme in sentence:
        word = morpheme["surface"]
        if word not in answer:
            answer[word] = 1
        else:
            answer[word] += 1
answer_sorted = sorted(answer.items(), key=lambda x: x[1], reverse=True)[:10]

labels = [ans[0] for ans in answer_sorted]
values = [ans[1] for ans in answer_sorted]
plt.figure(figsize=(8, 8))
plt.bar(labels, values)
plt.show()
