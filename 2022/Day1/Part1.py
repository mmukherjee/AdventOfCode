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
print ("Maximum Value is: " + str(max(arr_overall_count)))
