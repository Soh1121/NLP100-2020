input_file = "./input/ai.ja.txt"
with open(input_file) as rf:
    lines = rf.readlines()
lines = [line.rstrip() for line in lines]

ans = ""
for line in lines:
    if line == "":
        continue
    chars = list(line)
    for index, i in enumerate(chars):
        ans += i
        if index == len(chars) - 1:
            continue
        if i == "。" and chars[index + 1] != ")" and chars[index + 1] != "」":
            ans += "\n"
    ans += "\n"

output_file = "./output/ai.ja.txt"
with open(output_file, mode="w") as wf:
    wf.write(ans)
