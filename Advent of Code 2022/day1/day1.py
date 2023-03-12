input = open('day1input.txt','r')
# lines = (input.readline())
datasheet = []
# format the input into a usable format and append it to the datasheet list
for x in input:
    x=x.replace('\n','')
    datasheet.append(x)
# declare lists
packlists = []
elfpacks = []
# sort the datasheet into individual elf backpacks
for x in datasheet:
    if x != '':
        elfpacks.append(int(x))
        # print(elfpacks)
# sum the backpacks and make a list of backpack sums
    if x == '':
        elfpacksums = sum(elfpacks)
        print(elfpacksums)
        packlists.append(elfpacksums)
        elfpacks.clear()
packlists.sort()
print(packlists)
#print the biggest value in the lists
print ('max = ',packlists[-1])
#get the top 3
top3 = [packlists[-1],packlists[-2],packlists[-3]]
print('top 3 =', top3, 'sum = ', sum(top3))