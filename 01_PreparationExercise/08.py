def cipher(string):
    encyption = ""
    for i in list(string):
        if i.islower():
            encyption += chr((219 - ord(i)))
        else:
            encyption += i
    return encyption


test = "Hi He Lied Because Boron Could \
    Not Oxidize Fluorine. New Nations Might \
    Also Sign Peace Security Clause. Arthur \
    King Can."
encyption = cipher(test)
print(encyption)
normal = cipher(encyption)
print(normal)
