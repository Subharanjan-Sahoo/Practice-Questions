def electric(input1,input2,input3):
    input1 = input1[:input3]
    input2 = input2[:input3]
    str1 = []
    sum = 0
    for i in range(len(input2)):
        for j  in range(len(input2)):
            if i == j and  input2[j] == "P":
                str1.append(input1[i])
            elif i == j and input2[j] == "N":
                str1.append(-(input1[i])) 
    for i in range(len(str1)):
        sum += str1[i]
    print(sum*100)





input1 = list(map(int ,input().strip().split(",")))
input2 = input()
input3 =int(input())
electric(input1,input2,input3)