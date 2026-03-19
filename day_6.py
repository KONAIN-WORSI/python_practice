##lst = [8, 7, 6, 3, 4, 2, 1]
##
##for i in range(len(lst)):
##   for j in range(len(lst)):
##        if lst[j] > lst[i]:
##            lst[i], lst[j] = lst[j], lst[i]
##
##
##print(lst)


#lst = [2, 3, 6, 8, 9, 12, 15, 18, 24, 22, 33, 112, 77]
#divs_num = []

#for num in lst:
 #   if num % 2 == 0 or num % 3 == 0:
  #      divs_num.append(num)


#print(divs_num)


#lst = [10, 20, 25, 30, 40, 45, 50, 60, 80, 85, 100, 79]
#divs_num = []

#for num in lst:
  #  if num % 4 == 0 or num % 5 == 0:
 #       divs_num.append(num)


#print(divs_num)


##lst = [2, 3, 6, 8, 9, 12, 15, 18, 24, 22, 33, 112, 77]
##even_lst = []
##
##
##for num in range(len(lst)):
##    if num%2==0:
##        even_lst.append(lst[num])
##
##
##print(even_lst)


##lst = [2, 3, 6, 8, 9, 12, 15, 18, 24, 22, 33, 112, 77]
##odd_lst = []
##
##
##for num in range(len(lst)):
##    if num%2!=0:
##        odd_lst.append(lst[num])
##
##
##print(odd_lst)


##lst1 = ['a', 'b', 'c']
##lst2 = [1, 2, 3]
##
##lst3 = []
##
##if len(lst1) == len(lst2):
##    for i in range(len(lst1)):
##        lst3.append(lst1[i])
##        lst3.append(lst2[i])
##
##
##print(lst3)


##lst1 = ['A', 'H', 'M']
##lst2 = ['@', '#', '&']
##
##lst3 = []
##
##if len(lst1) == len(lst2):
##    for i in range(len(lst1)):
##        lst3.append(lst1[i])
##        lst3.append(lst2[i])
##
##
##print(lst3)


##lst1 = [1, 2, 3, 4, 5, 6]
##lst2 = [1, 2, 3, 4, 5, 6]
##
##sum_lst = []
##
##for i in range(len(lst1)):
##    add = lst1[i] + lst2[i]
##    sum_lst.append(add)
##
##
##print(sum_lst)



lst1 = ['a', 'b', 'c', 'd', 'e']
lst2 = ['f', 'g', 'h', 'i', 'j']

concat = []

for i in range(len(lst1)):
    add = lst1[i] + lst2[i]
    concat.append(add)

print(concat)
    
    
