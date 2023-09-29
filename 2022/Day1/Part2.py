# Read the input file
file1 = open('Day1/input.txt', 'r')
Lines = file1.readlines()
 
arr_overall_count = []
elf_cal_count = 0
for line in Lines:
    if (line == "\n"):
        # push the calorie count to the final array and reset the elf calorie count
        arr_overall_count.append(elf_cal_count)
        elf_cal_count = 0
    else:
        # increment the calorie count
        elf_cal_count = elf_cal_count + int(line.strip())

# sort in descending order
arr_overall_count.sort(reverse=True)
sum_top_three = arr_overall_count[0] + arr_overall_count[1] + arr_overall_count[2]
print ("Sum of top 3 values is: " + str(sum_top_three))
