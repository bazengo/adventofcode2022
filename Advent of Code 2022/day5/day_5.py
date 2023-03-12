
from pickle import TRUE
from re import X
from xml.dom.expatbuilder import parseString


f = readFile = open('input.txt')
z = f.readlines()

a = []
l1=[]
rcrates = []
lists = [[]for i in range (8)]
i = 0
y = 0
#print (lists)
#print(z)
for x in z:
    #print(len(x))
    if len(x) == 36:
        
    
        #print(x)
        n = 4
        crates = [x[i:i+n]for i in range(0, len(x),n)]
        #print(crates)
    if y < 8:
        for x in range(1):
            rcrates = [x.replace('\n','')for x in crates]
            rrcrates = [x.replace('[','')for x in rcrates]
            rrrcrates = [x.replace(']','')for x in rrcrates]
            rrrrcrates = [x.replace('    ','')for x in rrrcrates]
            rrrrrcrates = [x.replace(' ','') for x in rrrrcrates]
            #print(rrrrrcrates)
            y = y+1
        #print(list(crates))
        
            l1.append(rrrrrcrates)
o = []
for x in z:
    if len(x) < 25 and len(x) > 15:
        filtered = (''.join(filter(str.isdigit,x)))
        #print(filtered)
        if len(list(filtered)) == 3:
            operation = [int(filtered[0]),int(filtered[1]),int(filtered[2])]
            o.append(operation)
        else:
            c = (str(filtered[0]))
            d = (str(filtered[1]))
            operation = [int(str(c+d)),int(filtered[2]),int(filtered[3])]
            o.append(list(operation))     
n = 0
m = 0
sub = []    
main = []
for x in range(9):
    for x in range(8):
        
            t = (l1[n][m])
            if t != '':
                sub.append(t)
            n = n+1
            if n == 8:
                n = 0
                m = m+1

                
    sub.reverse()

    #print(sub)
    main.append(list(sub))
    sub.clear()


#for x in range(len(o)):
        #print(len(o))
crane = []
for x in o:
    #print(x)
    o1 = x[0]
    o2 = int(x[1]-1)
    o3 = x[2] -1
    print (o1, o2, o3)
    #for x in (range(o1)):
        #crane.append((str(main[o2][-1])))
        #print(crane)
        #main[o2].pop()
        #for x in crane:
            #main[o3].append(x)
        #print(main[o3])
        #crane.clear()
    print('from ', main[o2])
    for x in range(o1):
        crane.append(str(main[o2][-1]))
        main[o2].pop()
    crane.reverse()
    print('crane', crane)
    print('to',main[o3])
    for x in crane:
        main[o3].append(x)
    print('to',main[o3],'result')
    crane.clear()
        
    #print(crane)    
        
final=[]
for x in main:
    final.append(x[-1])
print(final)
