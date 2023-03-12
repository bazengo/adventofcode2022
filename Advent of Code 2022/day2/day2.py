f = open('day2input.txt')
# set the scorecard, 0 draw, 1,win, 2 loss
scoredict={
    0:3,
    1:6,
    2:0,
}

scorecard = []
scorepart2 = []
scorecardp2 = []
for x in f: # set the matchup values
    if 'A' in x:
        opponent=1
    if 'B' in x:
        opponent=2
    if 'C' in x:
        opponent=3

    if 'X' in x:
        protag=1
    if 'Y' in x:
        protag=2
    if 'Z' in x:
        protag=3
    # calculate a win loss or draw, 0=draw 1=win 2=loss
    winlossdraw=((protag-opponent)%3)
    # add the protag value to the wld value for a final score
    score = protag+scoredict.get(winlossdraw)
    print(score)
# add each score to a scorecard list
    scorecard.append(score)
    #part 2
    scorepart2 = 0
# print the sum of scores on the scorecard
print(sum(scorecard))
