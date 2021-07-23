def OddEven(input1):
    a = 0
    b = 0
    for i in range(len(input1)):
        if i % 2 == 0: 
            a = a + int(input1[i])
        else:
            b = b + int(input1[i])
    print(str((b - a))[1:])    




input1 = input("Enter the number: ")
OddEven(input1)