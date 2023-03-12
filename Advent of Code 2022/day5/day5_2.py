import re
with open('day5input.txt','r') as inp:
    lines=[x for x in inp]
    print(lines)
any = []
sublist = []
for line in lines:
    any = re.findall('[A-Z]|    ',line)
    if any:
        print(any)
    for x in any:
        sublist.append[any[x]]
    print(sublist)