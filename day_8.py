##lst = ['a', 'a', 'b', 'c', 'c', 'd', 'c', 'e', 'd', 'e']
##
##s = set(lst)
##uniq = list(s)
##
##new_lst = sorted(uniq, reverse=True)
##
##print(new_lst)


##lst = []
##
##m = int(input("Enter the number of row in the list: "))
##n = int(input("Enter the number of column in the list: "))
##
##
##for i in range(m):
##    row = []
##    for j in range(n):
##        if i == j:
##            row.append(1)
##        elif i < j:
##            row.append(2)
##        else:
##            row.append(3)
##
##    lst.append(row)
##
##
##print(lst)


##lst = []
##
##m = int(input("Enter the number of row in the list: "))
##n = int(input("Enter the number of column in the list: "))
##
##
##for i in range(m):
##    row = []
##    for j in range(n):
##        if i == j:
##            row.append(0)
##        elif i < j:
##            row.append(1)
##        else:
##            row.append(-1)
##
##    lst.append(row)
##
##
##print(lst)



a = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
b = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]

max_a = a[0][0]
min_a = a[0][0]


add_d = 0
add_above = 0
add_below = 0

for i in range(len(a)):
    for j in range(len(a[i])):
        if i == j:
            add_d += a[i][j]
        elif i < j:
            add_above += a[i][j]
        else:
            add_below += a[i][j]

        if i > max_a:
            max_a = i
        elif i < min_a:
            min_a = i

    
print("Addition of diagonal number: ", add_d)
print("Addition of above the diagonal number: ", add_above)
print("Addition of below the diagonal number: ", add_below)
print(max_a)
print(min_a)
    
        












    

