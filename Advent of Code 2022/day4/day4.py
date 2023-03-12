FileInput = open('day4input.txt')
FormattedInput = [((x.replace('\n',''))) for x in FileInput]
pairlists = [x.split(',') for x in FormattedInput]
answerp1, answerp2 = [], []
for x in pairlists:
    x[0], x[1] = (x[int(0)].split('-')), (x[int(1)].split('-'))
    elf1Min, elf1Max, elf2Min, elf2Max = int(x[0][0]),int(x[0][1]),int(x[1][0]),int(x[1][1])
    elf1Range, elf2Range, elfRangeIntersect= set(), set(), set()
    for x in range(elf1Min,elf1Max+1): elf1Range.add(x)
    for x in range(elf2Min,elf2Max+1): elf2Range.add(x)
    elfRangeIntersect = elf1Range.intersection(elf2Range)
    if elfRangeIntersect == elf1Range or elfRangeIntersect == elf2Range:
        answerp1.append(1)
    if (elfRangeIntersect)!=set():
        answerp2.append(1)
print('the answer to part 1 is: ',sum(answerp1))
print('the answer to part two is: ',sum(answerp2))