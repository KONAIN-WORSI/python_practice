##def sumOfOdd(n):
##    add = 0
##    for i in range(n + 1):
##        if i % 2 == 0:
##            continue
##        add += i
##
##    print(add)
##
##sumOfOdd(10)



##def sumOfOdd(n):
##    add = 0
##    for i in range(n + 1):
##        if i % 2 == 0:
##            add += i
##
##    print(add)
##
##sumOfOdd(10)



def checkMessage(word1, word2):
   l1 = list(word1)
   l2 = list(word2)

   l1.sort()
   l2.sort()

   if l1 == l2:
       print("This given words are an anagram")
   else:
       print("This given words are not an anagram")


a = input("Enter a word: ")
b = input("Enter a word: ")

checkMessage(a, b)



