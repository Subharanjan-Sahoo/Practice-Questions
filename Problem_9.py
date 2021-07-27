'''

Array and magic value

You are given an array a comprising n integers. You have to calculate the magic value of the array a Magic value of an array is equal to the difference between the sum of good integers in an array and the sum of the bad integers in an array.

Good Integers are the ones whose indexes are not changed in an array when sorted, rest are bed

Input format

First line of Input contain a single integer n

Second line of input contain space separated integers, elements of number.

'''

def diffrence(input1):
    input2 = list(map(int, input("Enter the element separate by space: ").strip().split(" ")))[:input1]
    temp = input2[:]
    good = 0 
    bad = 0 
    for i in range(len(input2)-1):
        for j in range(len(input2)-1):
            if input2[j] > input2[j+1]:
                input2[j] , input2[j+1] = input2[j+1] , input2[j]
    for k in range(len(temp)):
        if temp[k] == input2[k]:
            good += temp[k]
        else:
            bad += temp[k] 
    diffrenceingoodandbad  = ( good - bad)
    print("diffrenceingoodandbad = ",diffrenceingoodandbad)



input1 = int(input("Enter the Number of element: "))
diffrence(input1)