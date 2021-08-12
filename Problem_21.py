'''
Write A Program To Input String And Display Count Of All Permutations Of Strings Without Using Any Built In Functions

Input

abc

Output

6
'''
def Permutations(input1):
    length = len(input1)
    cumbination = 1
    for i in range(1,length+1):
        cumbination = i * cumbination
    print(cumbination)     

input1 = input()
Permutations(input1)