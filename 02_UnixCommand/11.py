file_name = "popular-names.txt"
with open(file_name) as f:
    text = f.read()
print(text.replace("\t", " "))
