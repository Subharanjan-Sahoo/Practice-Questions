"Sum of Digit"

"-----------------------Using For loop-------------------"

def SumOfDigit(input1):
    sum = 0
    for i in input1:
        sum = int(i) + sum
    print(sum)

input1 = input()
SumOfDigit(input1)


"----------------------Using n%number and n/number------------"

def SumofDigit(input1):
    sum = 0
    while(input1 > 0):
        sum += input1%10
        input1 = input1/10
    print(sum)
input1 = int(input())
SumofDigit(input1)     
    