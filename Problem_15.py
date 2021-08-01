def sumZero(input1):
    fact = 1
    count = 0
    for i in range(1,input1+1):
        fact = fact * i
        n = fact
    digits = [int(x) for x in str(n)]
    for i in digits:
        if i == 0:
            count =count + 1
    print(count)        


input1 = int(input("Enter the number: "))
sumZero(input1)