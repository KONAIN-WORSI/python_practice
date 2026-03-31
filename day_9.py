##word = input("Enter a word of yout choice: ")
##
##vowel = ['a', 'e', 'i', 'o', 'u']
##
##def isVowel(word):
##    vowel_l = "".join(vowel)
##    vowel_count = 0
##    consonant_count = 0
##    vowel_list = []
##    consonant_list = []
##    
##    for i in word:
##        if i in vowel_l:
##            vowel_list.append(i)
##            vowel_count += 1
##        else:
##            consonant_list.append(i)
##            consonant_count += 1
##
##    return vowel_list, consonant_list
##        
##
##
##
##print(isVowel("konain"))
##

##def add_num():
##    number = input("Enter the number in string: ").lower()
##    add=0
##    for i in number:
##        add+=int(i)
##
##    print(add)
##
##add_num()
        
target = int(input("Enter a target number: "))
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def isTen(num, target):
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            if num[i] + num[j] == target:
                return num[i], num[j]

    return None

print(isTen(number, target))
