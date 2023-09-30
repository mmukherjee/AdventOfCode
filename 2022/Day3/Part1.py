# Read the input file
file1 = open('Day3/input.txt', 'r')
Lines = file1.readlines()
count_priority = 0


for line in Lines:
    first_half  = line.strip()[:len(line.strip())//2]
    second_half = line.strip()[len(line.strip())//2:]
    # print (first_half)
    # print (second_half)
    first_half = set(first_half)
    second_half = set(second_half)
    common_character = ''.join(sorted(first_half.intersection(second_half)))
    if common_character.islower():
        common_character_priority = ord(common_character)-96
    else:
        common_character_priority = ord(common_character)-38
    # print (common_character_priority)
    count_priority = count_priority + common_character_priority

print ("Count priority is: " + str(count_priority))




