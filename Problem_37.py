'''
Rishab owns a rectangular plot of land . Due to certain financial problems , he wishes to sell some parts of his plot. Rishab finds out that square shaped plots sell better than rectangular ones . With this in mind, he decides to divide his plot into minimum possible square plots so that he can get maximum profit . All the square plots have the same dimension.

Given the dimensions of his plot , Write a Program to calculate the minimum number of square plots.

Input
The first line of input consists of two integers L and B which denotes the length and breadth of the rectangular plot.

Output
Output is a single line which denotes the minimum number of square plots that can be formed

Test Case 1

Input (stdin)
4 6

Expected Output
6
Test Case 2

Input (stdin)
10 15

Expected Output
6

'''
def minimumSqure(input1):
    a = input1[0]
    b = input1[1]

    result = 0
    rem = 0

    if (a>b):
        a,b = b,a

    while(b>0):
        result += int(a/b)
        
        rem = int(a % b)
        a = b
        b = rem
    print(result)


input1 = list(map(int , input().strip().split(" ")))[:2]
minimumSqure(input1)

