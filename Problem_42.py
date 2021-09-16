'''

Problem Statement and Intrases

Problem Description

A supermarket maintains a pricing format for all its products. A value N is printed on each product. When the scanner reads the value N on the item, the product of all the digits in the value N is the price of the item. The task here is to design the software such that given the code of any item N the product (multiplication) of all the digits of value should be computed (price).

Input

5244

Output

160

Explanation

From the input above

Product of the digits 5,2,4,4

5*2*4*4=160

Hence, output is 160


'''


def maintains(N):
    Sum = 1
    for i in range(len(N)):
        Sum = int(N[i]) * Sum
    print(Sum)

N = input()    
maintains(N)