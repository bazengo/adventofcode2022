import re
FileInput = open('day5input.txt')
FormattedInput = [x.replace('\n','') for x in FileInput]
stack, cratelist = list(), list()
for line in FormattedInput:
    if len(line)==35:
        crates = [line[chunk:chunk+4] for chunk in range(0,len(line),4)]
        cratelist.append(crates)
FormattedCrateList = list()
for n in range(0,9):
    sublist = []
    for x in cratelist:
        any = re.search('[A-Z]',x[n])
        if any:
            x[n] = (any.group())
            sublist.append(x[n])
    sublist.reverse()
    FormattedCrateList.append(sublist)
for x in FormattedCrateList:
    print(x)
arguments = (0,0,0)
def movecrates1(inst):
    times, sender, reciever = inst
    for x in range(0,times):
        target = FormattedCrateList[sender-1][-1]
        FormattedCrateList[sender-1].pop()
        FormattedCrateList[reciever-1].append(target)
def movecrates2(inst):
    times, sender, reciever = inst
    target = []
    for x in range(0,times):
        print(x)
        target.append(FormattedCrateList[sender-1][-x])
        FormattedCrateList[sender-1].pop()
        print(FormattedCrateList[reciever-1])
        for x in target:
            FormattedCrateList[reciever-1].append(target)
    print(target)

for line in FormattedInput:
    if 'move' in line:
        instructions = (re.findall('[0-9][0-9]|[0-9]',line))
        for x in instructions:
            arguments = int(instructions[0]),int(instructions[1]),int(instructions[2])
        movecrates1(arguments)
        # movecrates2(arguments)
answerp1 = list()
for x in FormattedCrateList:
    answerp1.append(x[-1])
print('the answer is: ',answerp1 )