import pandas as pd


df = pd.read_csv("./output/64.txt", sep=" ", header=None)
sem = df[~df[0].str.contains("gram")]
syn = df[df[0].str.contains("gram")]
print("意味的アナロジー正解率：", (sem[4] == sem[5]).sum() / len(sem))
print("文法的アナロジー正解率：", (syn[4] == syn[5]).sum() / len(syn))
