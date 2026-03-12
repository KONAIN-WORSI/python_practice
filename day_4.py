
#name = []
#pricel = []
#sub_total = 0

#while(True):
    #product_name = input("Enter the name of the product: ")
   # price = int(input("Enter the price of the product: "))
  #  permission = input("Do you want to continue shopping? (y/n): ")
 
    #if product_name == " ":
 #       print("Please enter the name of the product: ")
     #   continue
   # elif price < 0:
     #   print("Please enter the price of your selected product")
       # continue
    
   # name.append(product_name)
    #pricel.append(price)
    #sub_total += price

   # if permission == "y":
      #  continue
   # elif permission == "n":
       # for i in range(len(name)):
      #      print(name[i], pricel[i])
       # print("Your total price of shopping: ", sub_total)
        #break



#numbers = [1, 2, 3, 4, 5, 66, 4, 3 ,4, 6, 8, 67, 86 ,5, 7]

#unique_number = []

#for num in numbers:
 #   if num not in unique_number:
  #      unique_number.append(num)


#print("Distinct number from the numbers lists: ", unique_number)


numbers = [1, 2, 3, 4, 5, 66, 4, 3 ,4, 6, 8, 67, 86 ,5, 7]
reverse_numbers = []

for i in range(len(numbers)-1,-1,-1):
    reverse_numbers.append(numbers[i])

print(reverse_numbers)
