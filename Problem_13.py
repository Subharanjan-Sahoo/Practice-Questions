'''

Write a function to find all the words in a string which are palindrome

Note: A string is said to be a palindrome if the reverse of the string is the same as string. For example, "abba" is a palindrome, but "abbe" is not a palindrome.

Input Specification:

input1: string

input2: Length of the String

Output Specification:

Retum the number of palindromes in the given string

Example 1:

inputt: this is level 71 
input2: 16

Output 1

'''

def palondrom(input1):
    input2 =list(input("input the string: ").strip().split(" "))[:input1]
    count = 0
    for i in input2:
        if i == i[::-1]:
            count = count + 1
    print(count)       





input1 =int(input("Enter the number of Word: "))
palondrom(input1)