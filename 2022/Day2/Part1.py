def calculate_score(opponent, myself):
#   A = X = Rock
#   B = Y = Paper
#   C = Z = Scissors
#   Rock defeats Scissors, 
#   Scissors defeats Paper, 
#   Paper defeats Rock. 
#   If both players choose the same shape, the round instead ends in a draw.
    score = 0
    global total_score
    if myself == 'X':
        score = 1
    if myself == 'Y':
        score = 2
    if myself == 'Z':
        score = 3
    if ((opponent == 'A' and myself == 'X') or (opponent == 'B' and myself == 'Y') or (opponent == 'C' and myself == 'Z')):
        # draw
        score = score + 3
    if ((myself == 'X' and opponent == 'C') or (myself == 'Z' and opponent == 'B') or (myself == 'Y' and opponent == 'A')):
        # I win
        score = score + 6

    # print("Score is " + str(score))
    total_score = total_score + score

# Read the input file
file1 = open('Day2/input.txt', 'r')
Lines = file1.readlines()
total_score = 0
 
for line in Lines:
    opponent_selection = line.strip()[0]
    my_selection = line.strip()[2]
    # print (opponent_selection, my_selection)
    calculate_score (opponent_selection, my_selection)

print("Total Score is " + str(total_score))



