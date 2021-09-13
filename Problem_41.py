'''
Problem Statement: Find the 15th term of the series?

0,0,7,6,14,12,21,18, 28

INPUT = 15

OUPUT = 49

Explanation:

In this series the odd term is increment of 7 (0, 7, 14, 21, 28, 35  - - - - - - - - - - - -) 

and even term is a increment of 6 (0, 6, 12, 18, 24, 30 - - - - - - - - - -}

'''


def FindSeries(term):
    list1 = [0,0]
    numEVEN = 0
    numODD = 0
    for i in range(term):
        if  i % 2 == 0:
            numEVEN = numEVEN + 6 
            list1.append(numEVEN)
        else:
            numODD = numODD + 7 
            list1.append(numODD)
    print(list1[term])            



term = int(input())
FindSeries(term)