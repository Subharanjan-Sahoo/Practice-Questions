'''
Given an array of integers representing measurements in inches, write a program to calculate the total of measurements in feet. Ignore the measurements those are less than a feet (e.g. 10)

Note:

You are expected to write code in the find TotalFeet function only which will receive the first parameter as the number of items in the array and second parameter as the array itself. You are not required to take input from the console.

Example

Finding the total measurements in feet from a list of 5 numbers

Input

input1: 5

input2: 18 11 27 12 14

Output

6.833333333333


'''
def findTotalFeet(input1 , input2 ):
    sum = 0
    for i in range (input1):
        sum = input2[i] + sum
    print(sum/12)      






input1 = int(input())
input2 = list(map(int , input().strip().split(" ")))[:input1]
findTotalFeet(input1 , input2)