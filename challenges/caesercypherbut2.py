riddle = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
from string import ascii_lowercase
for x in riddle:
    if x.isalpha():
        i = ascii_lowercase.find(x)
        i = (i + 2) % 26
        letter = ascii_lowercase[i]
        print(letter,end='')
    else:
        print(x,end = '')
