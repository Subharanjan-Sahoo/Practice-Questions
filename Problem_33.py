'''
Write a program to calculate and return the sum of distances between the adjacent numbers in an array of positive integers

Note:

You are expected to write code in the find TotalDistance function only which will receive the first parameter as the number of items in the array and second parameter as the array itself. You are not required to take input from the console

Example

Finding the total distance between adjacent items of a list of 5 numbers

Input input1: 5

input2: 10 11 7 12 14

Output

12

Explanation

The first parameter (5) is the size of the array. Next is an array of integers. The total of distances is 12 as per the calculation below

11-7-4

7-12-5

12-14-2 Total distance 1+4+5+2= 12

'''
def findTotalDistance(input1):
    input2 = list(map(int,input().strip().split(" ")))[:input1]
    sum = 0
    for i in range(input1):
        for j in range(input1):
            if i+1 == j:
                sum = (abs(input2[i] - input2[j])) + sum
    return sum 


input1 = int(input())
print(findTotalDistance(input1))