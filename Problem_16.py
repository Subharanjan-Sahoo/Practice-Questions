def jump(input1):
    count = 0
    while input1 != 0 :
        if input1 % 2 == 0:
            input1 = input1 // 2
            #print(input1)
            count += 1
        else:
            input1 = input1 - 1
            #print(input1)
            count += 1 
    print(count)



input1 = int(input("Enter the Number: "))
jump(input1)