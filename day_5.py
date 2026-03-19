lst = [5, 2, 9, 1, 6]

sorted_flag = False

while sorted_flag == False:
    num_swaps = 0

    for i in range(-1, -1 , len(lst)):
        if lst[i] > lst[i - 1]:
            print("Before swaps: ", lst[i], lst[i - 1])
            tmp = lst[i - 1]

            lst[i - 1] = lst[i]

            lst[i] = tmp
            print("After swap: ", lst[i - 1], lst[i])
            num_swaps = num_swaps + 1


    if num_swaps == 0:
        sorted_flag = True
    else:
        sorted_flag = False



print()
print("Descending Sorted List: ", lst)

