'''
Write a program to calculate and return the sum of distances between the adjacent numbers in an array of positive integers.

Note:

You are expected to write code in the find TotalDistance function only which will

receive the first parameter as the number of items in the array and second

parameter as the array itself. You are not required to take input from the console

Example

Finding the total distance between adjacent items of a list of 5 numbers

Input

input1: 5 input2 10 11 7 12 14

Output

12

'''
def Diffrence(input1):
    a = 0
    b = 0 
    sub=0
    input2 = list(map(int, input("Enter the list of numbers: ").strip().split(" ")))[:input1]
    # intr1 = int(input2)
    for i in range(len(input2)):
        j = i+1
        #print(i)
        #print(input2[i+1])
       #for j in range(i+1,len(input2)):
        if j != len(input2):
            sub = input2[i] - input2[j]
           # print(sub)
            if sub < 0 :
                a = sub + a    
            else:
                b = sub + b
    print(b+(-(a)))







input1 =int(input("Enter the number: "))
Diffrence(input1)
