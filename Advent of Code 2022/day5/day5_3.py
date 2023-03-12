import re
with open('day5input.txt') as inp:
    any = inp.read().split('\n')
for line in any:
    if len(line) == 35:
        # print(line)
        lista = re.findall('[A-Z|   ]',line)
        if lista:
            print(lista)