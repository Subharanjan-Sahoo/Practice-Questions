'''
Tom has an array of distinct integars 'a1', 'a2', 'a3', 'a4', .....,'an' of size 'n'.

Tom defines that value of a subset of array 'a' is maximum number in

that subset.

Calculate product of values of all possible non-empty subsets of array'a'.

Input Format

First line contains n (Number of elements in an array).

Next n lines contain n distinct integars a1, a2, a3, a4,......, an.

Output Format

Print the answer % 1000000007

Constraints

1 <= n <= 10^3

1 <= ai <= 100 All ai and aj are pairwise distinct ( =))

Sample Example 1:

Input

2

3

7

Output

1

Explanation

val( (3))-3

val (7))-7

val( (3, 7))=7 answer = (3-7-7)=147 % 1000000007 = 147

'''

def maxproduct(list1,n):
    maximum = max(list1)
    product = 1
    for i in range(n):
        if i < n: 
            product = list1[i] * product    
    print((product*maximum) % 1000000007)
            




n = int(input("Enter the number of element: "))
list1 = list(int(n) for n in input("Enter the list items separated by space ").strip().split())[:n]
maxproduct(list1,n)