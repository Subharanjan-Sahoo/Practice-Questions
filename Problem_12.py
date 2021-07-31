'''
Write a function to remove duplicate elements from an array and retu with unique integer values only.

Input Specification:

inputt: An integer array containing numbers input2: Length of the above integer array

Output Specification:

Return an integer array after removal of duplicate values

Example 1:

input1: (11,11,11,13,13,20) input2: 6

Output: (11,13,20)

'''
def DuplicateValue(input1):
    input2 = list(map(int ,input("Enter the element separate by , : ").strip().split(",")))[:input1]
    print(set(input2))






input1 = int(input("Enter the no of element: "))
DuplicateValue(input1)
    