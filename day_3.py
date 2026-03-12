#number = int(input("Enter the number: "))

#if(number % 2 == 0):
  #  print("Its a even number!")
#else:
 #   print("Its a odd number!")


#num1 = int(input("Enter the first number: "))
#num2 = int(input("Enter the second number: "))
#num3 = int(input("Enter the third number: "))


#if(num1 > num2 & num1 > num3):
#    print(num1, "is the greatest number!")
#elif(num2 > num1 & num2 > num3):
#    print(num2, "is the greatest number!")
#else:
 #   print(num3, "is the greatest number!")

#num1 = int(input("Enter the first number: "))
#num2 = int(input("Enter the second number: "))
  
#while(num2 != 0):
 #   t = num2
  #  num2 = num1 % num2
   # num1 = t


#print(num1 , "is the greatest common divisor")


#num = int(input("Enter the positive integer number: "))
#factorial = 1

#if(num > 0):
 #   while(num != 0):
  #      factorial = factorial * num
   #     num = num - 1
    

#print(factorial, "is the total factorial of the given number!")



#num = int(input("Enter the number to be append in the list: "))
#lists  = []

#for i in range(1, num + 1):
 #   lists.append(i)

#oddadd = 0
#evenadd = 0

#for n in lists:
 #   if(n % 2 == 0):
  #      evenadd += n
   # else:
    #    oddadd += n
        

#print("The sum of even number: ", evenadd, "The sum of odd number: ", oddadd)

number = int(input("Enter a number: "))

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")
else:
    print(number, "is not a prime number")

    
    
