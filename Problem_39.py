def sumFactorial(input1):
    sum = 0
    for i in range(len(input1)):
        factorial = 1
        for j in range(1,int(input1[i])+1):
            factorial =  factorial * j
        sum = sum + factorial   
    if sum == int(input1):
        print('Yes')
    else:
        print('No')    

                




input1 = input()
sumFactorial(input1)