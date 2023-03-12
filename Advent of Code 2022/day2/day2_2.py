Input = open('day2input.txt')
formattedlist= list()
mode = str()
for item in Input:
    item = item.replace('\n','')
    formattedlist.append(item)
# print(formattedlist)
while mode != 'part1' and mode != 'part2':
    print('to solve for part 1 or part 2, enter "part1" or "part2"...')
    mode = (input())
    
Part1Scores = {
    'B X':1, #paper vs rock = loss = 0 + 1 = 1
    'C Y':2, #scissors vs paper = loss = 0 + 2 = 2
    'A Z':3, #rock vs scissors = loss = 0 + 3 = 3
    'A X':4, #rock vs rock = draw = 3 + 1 = 4
    'B Y':5, #paper vs paper = draw = 3 + 2 = 5
    'C Z':6, #scissors vs scissors = draw = 3 + 3 = 6
    'C X':7, #paper vs rock = win = 6 + 1 = 7
    'A Y':8, #rock vs paper = win = 6 + 2 = 8
    'B Z':9, #paper vs scissors = win = 6 + 3 + 9
}
Part2Scores = {
    'B X':1, #lose to paper = play rock
    'C X':2, #lose to scissors = play paper = 0 + 2 = 2
    'A X':3, #lose to rock = play scissors = 0 + 3 = 3
    'A Y':4, #draw to rock = play rock = 3 + 1 = 4
    'B Y':5, #draw to paper = play paper = 3 + 2 = 5
    'C Y':6, #draw to scissors = play scissors 3 + 3 = 6
    'C Z':7, #win to scissors = play rock = 6 + 1 = 7
    'A Z':8, #win to rock = play paper 6 + 2 = 8
    'B Z':9, #win to paper = play scissors = 6 + 3 = 9
}
if mode == 'part1':
    part1sum = []
    for x in formattedlist:
        part1sum.append(Part1Scores.get(x))
    print('the answer is: ',sum(part1sum))
if mode == 'part2':
    part2sum=[]
    for x in formattedlist:
        part2sum.append(Part2Scores.get(x))
    print('the answer is: ',sum(part2sum))

# part 1 answer = 12156
# part 2 answer = 10835