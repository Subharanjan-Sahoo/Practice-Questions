'''

Write a program to return the difference between the largest and smallest number from an array of positive integers.

input1: 5
input2: 10 11 7 12 14

Output:
--------

7

'''

def findLargeSmallDifference(input1):
    input2 = []
    diffrence =  0 
    input2 = list(map(int, input("enter the element sparate by value: ").strip().split(" ")))[:input1]
    for i in range(len(input2)-1):
        for j in range(len(input2)-1):
            if input2[j] > input2[j+1]:
                input2[j],input2[j+1] = input2[j+1],input2[j]
            else:
                diffrence = input2[len(input2)-1] - input2[0]
    print(diffrence)
            
input1 = int(input("Enter the Number of element: "))
findLargeSmallDifference(input1)