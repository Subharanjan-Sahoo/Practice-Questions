def Oparater(input1):
    for i in range(len(input1)):
        num = int(input1[0])
        for i in range(len(input1)):
            if input1[i] == "A":
                num = num and int(input1[i+1])
            if input1[i] == "B":
                num = num or int(input1[i+1])
            if input1[i] == "C":
                num = num ^ int(input1[i+1])
    print(num)
input1 = input()
Oparater(input1)   