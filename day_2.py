a = int(input("Enter the first number(a): "))
b = int(input("Enter the second number(b): "))

print("Before Swapping;")
print("a: ", a)
print("b: ", b)

a, b = b, a
print("After Swapping;")
print("a: ", a)
print("b: ", b)

item1 = input("Enter the name of first product: ")
price1 = int(input("Enter the price of first product: "))

item2 = input("Enter the name of second product: ")
price2 = int(input("Enter thr price of second product: "))

item3 = input("Enter the name of third product: ")
price3 = int(input("Enter the price of third product: "))

total_cost = price1 + price2 + price3
tax_amount = total_cost * 0.13

total_amount = total_cost + tax_amount

print("--------Total Bill----------")
print("Item name: ",item1," Price: ", price1, end="")
print("\nItem name: ",item2, " Price: ", price2, end="")
print("\nItem name: ",item3, " Price: ", price3, end="")
print("\nTotal cost: ", total_cost, end="")
print("\nTax amount: ", tax_amount, end="")
print("\nTotal amount with tax amount is ", total_amount)


subject1 = input("Enter the name of the subject: ")
marks1 = int(input("Enter the marks: "))

subject2 = input("Enter the name of the subject: ")
marks2 = int(input("Enter the maerks of the subject: "))

subject3 = input("Enter the name of the subject: ")
marks3 = int(input("Enter the marks of the subject: "))

total_marks = marks1 + marks2 + marks3
avg = total_marks / 3

print("------Report Card------")
print("Subject: ", subject1," Marks: ", marks1, end="")
print("\nSubject: ", subject2, " Marks: ", marks2, end="")
print("\nSubject: ", subject3, " Marks: ", marks3, end="")
print("\nTotal Marks: ", total_marks, end="")
print("\nAverage: ", avg, end="")


print(type(5.0))
