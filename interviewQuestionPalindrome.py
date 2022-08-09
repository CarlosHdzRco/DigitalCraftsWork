
num = input('Enter Number: ')

strNum = str(num)

isPalindrome = True

back = len(strNum)-1
for front in strNum:
    if front != strNum[back]:
        isPalindrome = False
    back -= 1

if(isPalindrome == True):
    print('The number %s is a Palindrome' % num)
elif(isPalindrome == False):
    print('The number %s is not a Palindrome' % num)


# # Write a program to check if the given number is a palindrome number.
# # A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers

# userNum = (input('Please type in a palindrome number: '))
# reversedInput = (userNum[::-1])

# # for x in userNum:
# if userNum == reversedInput:
#     print('%s is a palindrome' % userNum)
# else:
#     print('%s is not a palindrome' % userNum)

# # Haven't complete for non-numbers input



# word = input("Enter a word. ")
# half = len(word)/2
# half = int(half)
# print(word[0:half+1])
# print(word[len(word):half-1:-1])

# if word[0:half+1] == word[len(word):half-1:-1]:
#     print("It is a palindrome. ")
# else:
#     print("Not a palindrome. ")


# numbers = (input('Please enter a number that has at least three characters: '))

# try:
#     checkInt = int(numbers)
#     if len(numbers) > 2:
#         palindrome = numbers[::-1]
#         if numbers == palindrome:
#             print('The number %s is a palindrome!' % numbers)
#         else:
#             print('The number %s is not a palindrome!' % numbers)
#     else:
#         print('Invalid entry.')
# except:
#     print('Invalid entry.')