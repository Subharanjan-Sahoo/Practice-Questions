'''
Statement:

Given two numbers n1 and n2. Find prime numbers between n1 and n2, then make all possible

unique combinations of numbers from the prime numbers list you found in step 1.

From this new list, again find all prime numbers. Find smallest (a) and largest (b) number from

the 2nd generated list, also count of this list.

Consider smallest and largest number as the 1st and 2nd number to generate Fibonacci series respectively till the count (number of primes in the 2nd list).

Print the last number of a Fibonacci series as an output

Input Format:

One line containing two space separated integers n1 and n2.

Output Format:

umber of a generated Fibonacci series.

Constraints:

2<=n1 and n2<=100 n2-n1 >= 35

'''

list1 = []
list2 = []
def PrimeFiboacci(input1):
    A = input1[0]
    B = input1[1]
    for i in range(A,B):
        if Prime(i) == True:
            list1.append(i)
    concatnumber(list1)        



def Prime(i):
    for j in range(2,i):
        if i % j == 0:
            return False
    return True   


def concatnumber(list1):
    for i in range(len(list1)):
        for j in range(len(list1)):
            if i != j:
                add = int(str(list1[i])+str(list1[j])) 
                if Prime(add) == True:
                    list2.append(add)

                
input1 = list(map(int , input().strip().split(" ")))[:2]
PrimeFiboacci(input1)
print(sum(list2))
