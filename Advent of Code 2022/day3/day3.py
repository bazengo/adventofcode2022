FileInput = open('day3input.txt')
FormattedInput=list()
for x in FileInput:
    x = x.replace('\n','')
    FormattedInput.append(x)
commonchars = list()
for x in FormattedInput:
    first, second = set(x[:len(x)//2]), set(x[len(x)//2:])
    commonchar =  (first.intersection(second))
    commonchars.append(list(commonchar)[0])
lettermapping = dict(zip(range(ord('a'),ord('z')+1), range(1,27)))
lettermapping.update(dict(zip(range(ord('A'),ord('Z')+1), range(27,53))))
lista = list()
for x in commonchars:
    lista.append(lettermapping.get(ord(x)))
print('the answer to part one is: ',sum(lista))
setintersects = list()
for id_x, x in enumerate(FormattedInput):
    if id_x % 3==0:
        set1, set2, set3 = set(FormattedInput[id_x]), set(FormattedInput[id_x+1]), set(FormattedInput[id_x+2])
        setintersect = list(set3.intersection(set1.intersection(set2)))[0]
        setintersects.append(setintersect)
listb = list()
for x in setintersects:
    listb.append(lettermapping.get(ord(x)))
print('the answer to part two is: ',sum(listb))