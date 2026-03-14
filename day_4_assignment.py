
#  Question 1 

# num = int(input("Enter the number to be append in the list: "))
# lists  = []

# for i in range(1, num + 1):
#    lists.append(i)

# oddadd = 0
# evenadd = 0

# for n in lists:
#    if(n % 2 == 0):
#        evenadd += n
#    else:
#        oddadd += n

# print("The sum of even number: ", evenadd, "The sum of odd number: ", oddadd)

# Question 2
# num = int(input("Enter a number: "))

# num_list  = []

# if num > 1:
#     for i in range(1, num + 1):
#         num_list.append(i)

# for i in range(len(num_list)):
#     minimum = num_list[0]
#     if num_list[i] < minimum:
#         minimum = num_list[i]
#     elif num_list[i] > minimum:
#         maximum = num_list[i]



# print(maximum, "is the maximum number in the list!")
# print(minimum, "is the minimum number in the list!")
# print(num_list)

# Question 3
# n = int(input("Enter the number of Fibonacci numbers to generate: "))
# fibonacci = []

# if n >= 1:
#     fibonacci.append(1)
# if n >= 2:
#     fibonacci.append(1)

# for i in range(2, n):
#     next_num = fibonacci[i-1] + fibonacci[i-2]
#     fibonacci.append(next_num)

# print("Fibonacci sequence:", fibonacci)

# Question 4
# numbers = [1, 2, 3, 4, 5, 66, 4, 3 ,4, 6, 8, 67, 86 ,5, 7]

# unique_number = []

# for num in numbers:
#    if num not in unique_number:
#        unique_number.append(num)

# print("Distinct number from the numbers lists: ", unique_number)

# Question 5
# numbers = [1, 2, 3, 4, 5, 66, 4, 3 ,4, 6, 8, 67, 86 ,5, 7]
# reverse_numbers = []

# for i in range(len(numbers)-1,-1,-1):
#     reverse_numbers.append(numbers[i])

# print("Reverse numbers: ", reverse_numbers)

# Question 6
# lists = [1, 2, 6, 4, 5, 7, 6, 7, 8, 1, 4, 5]

# counts = {}
# for num in lists:
#     if num in counts:
#         counts[num] += 1
#     else:
#         counts[num] = 1

# more_than_once = 0
# for num in counts:
#     if counts[num] > 1:
#         print(f"{num} appears {counts[num]} times")
#         more_than_once += 1
# print(f"Total numbers that appear more than once: {more_than_once}")



# Question 7
# name = []
# pricel = []
# qnty = []
# sub_total = 0

# while(True):
#     product_name = input("Enter the name of the product: ")
#     price = int(input("Enter the price of the product: "))
#     quantity = int(input("Enter the quantity of the product: "))

#     permission = input("Do you want to continue shopping? (y/n): ")
 
#     if product_name == " ":
#        print("Please enter the name of the product: ")
#        continue
#     elif price < 0:
#        print("Please enter the price of your selected product")
#        continue
#     elif quantity < 0:
#         print("Please enter the quantity of your selected product")
#         continue
    
#     name.append(product_name)
#     pricel.append(price)
#     qnty.append(quantity)
#     sub_total += price * quantity
#     vat = sub_total * 0.13
#     total_cost = sub_total + vat

#     if permission == "y":
#        continue
#     elif permission == "n":
#        for i in range(len(name)):
#            print(name[i], pricel[i], qnty[i])
#        print("Your total price of shopping: ", sub_total)
#        print("VAT (13%): ", vat)
#        print("Your total price of shopping with 13% VAT: ", total_cost)
#        break

# Question 8
# students = []
# subjects = []

# num_subjects = int(input("Enter the number of subjects: "))
# for i in range(num_subjects):
#     subject = input(f"Enter the name of subject {i+1}: ")
#     subjects.append(subject)

# student_name = input("Enter the student's name: ")
# marks = []
# for subject in subjects:
#     mark = float(input(f"Enter marks obtained in {subject}: "))
#     marks.append(mark)

# students.append({'name': student_name, 'marks': marks})

# highest = max(marks)
# lowest = min(marks)
# average = sum(marks) / len(marks)

# if average >= 90:
#     grade = 'A'
# elif average >= 80:
#     grade = 'B'
# elif average >= 70:
#     grade = 'C'
# elif average >= 60:
#     grade = 'D'
# else:
#     grade = 'F'

# print(f"\nStudent: {student_name}")
# print(f"Subjects: {subjects}")
# print(f"Marks: {marks}")
# print(f"Highest mark: {highest}")
# print(f"Lowest mark: {lowest}")
# print(f"Average mark: {average:.2f}")
# print(f"Grade: {grade}")



# Question 9
numbers = []
n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Ascending order
asc_numbers = numbers.copy()
for i in range(len(asc_numbers)):
    for j in range(i + 1, len(asc_numbers)):
        if asc_numbers[i] > asc_numbers[j]:
            asc_numbers[i], asc_numbers[j] = asc_numbers[j], asc_numbers[i]

# Descending order
desc_numbers = numbers.copy()
for i in range(len(desc_numbers)):
    for j in range(i + 1, len(desc_numbers)):
        if desc_numbers[i] < desc_numbers[j]:
            desc_numbers[i], desc_numbers[j] = desc_numbers[j], desc_numbers[i]

print("Original list:", numbers)
print("Ascending order:", asc_numbers)
print("Descending order:", desc_numbers)