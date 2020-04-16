file_name = "popular-names.txt"
output_file1 = "output/col1.txt"
output_file2 = "output/col2.txt"
output_files = [output_file1, output_file2]

col1 = []
col2 = []
with open(file_name) as rf:
    for line in rf:
        item1 = line.split()[0]
        item2 = line.split()[1]
        col1.append(item1)
        col2.append(item2)
cols = [col1, col2]

for output_file, col in zip(output_files, cols):
    with open(output_file, mode='w') as wf:
        wf.write("\n".join(col) + "\n")
