col1_file = "output/col1.txt"
col2_file = "output/col2.txt"
cols_file = "output/cols.txt"
col_files = [col1_file, col2_file]

cols = []
for file_name in col_files:
    with open(file_name) as rf:
        cols.append(rf.readlines())

output = ""
for col1, col2 in zip(cols[0], cols[1]):
    output += col1.rstrip() + "\t" + col2.rstrip() + "\n"

with open(cols_file, mode='w') as wf:
    wf.write(output)
