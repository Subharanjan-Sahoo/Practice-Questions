"Palindrome"

'''--------------------Using Slicing------------------'''

def palindrome(input1):
    temp = input1[:]
    temp2 = input1[::-1]
    if temp2 == temp:
        print("it is palindrome")
    else:
        print("It is not palindrome")    

input1 = input()   
palindrome(input1) 



'''-------------------Using For Loop----------------------'''
def palindrome(input1):
    temp= input1[:]
    string = []
    for i in range(len(input1),0,-1):
         string.append(input1[i])
         print(string) 

input1 = input()
palindrome(input1)