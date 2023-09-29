def calculate_score(opponent, myself):
#   A = Rock
#   B = Paper
#   C = Scissors
#   A = 1
#   B = 2
#   C = 3
#   X means you need to lose, 
#   Y means you need to end the round in a draw, 
#   Z means you need to win
#   Rock defeats Scissors, 
#   Scissors defeats Paper, 
#   Paper defeats Rock. 
    score = 0
    global total_score
    if myself == 'X':
        # I have to lose
        if opponent == 'A':
            # I have to be a scissor
            score = 0 + 3
        if opponent == 'B':
            # I have to be a rock
            score = 0 + 1
        if opponent == 'C':
            # I have to be a paper
            score = 0 + 2
    if myself == 'Y':
        # I have to draw
        if opponent == 'A':
            # I have to be a rock
            score = 3 + 1
        if opponent == 'B':
            # I have to be a paper
            score = 3 + 2
        if opponent == 'C':
            # I have to be a scissor
            score = 3 + 3
    if myself == 'Z':
        # I have to win
        if opponent == 'A':
            # I have to be a paper
            score = 6 + 2
        if opponent == 'B':
            # I have to be a scissors
            score = 6 + 3
        if opponent == 'C':
            # I have to be a rock
            score = 6 + 1

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



