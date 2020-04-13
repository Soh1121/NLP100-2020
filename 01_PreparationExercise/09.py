import random

input_line = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
words_list = input_line.split()
ans = []
for i in words_list:
    if len(i) <= 4:
        ans.append(i)
        continue
    char = list(i)
    middle_char = char[1:len(i) - 1]
    ans.append(char[0] + "".join(random.sample(middle_char, len(middle_char))) + char[-1])
print(" ".join(ans))
