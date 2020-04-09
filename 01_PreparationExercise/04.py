element_symbol = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
table = str.maketrans('', '', ',.')
words = element_symbol.translate(table).split()

element_symbol_dict = {}
single_chars = [i - 1 for i in [1, 5, 6, 7, 8, 9, 15, 16, 19]]
for index, word in enumerate(words):
    length = 1 if index in single_chars else 2
    element_symbol_dict[word[:length]] = index + 1
print(element_symbol_dict)
