print("Printing current and previous number and their sum in a range(10)")
previous_num = 0

# Loop from 1 to 10 
for i in range(1, 11):
    x_sum = previous_num + i 
    print("current number", i, "previous number ", previous_num," sum: ", x_sum)
    # modify previuos number 
    # set it to the current number 
    previous_num = i
