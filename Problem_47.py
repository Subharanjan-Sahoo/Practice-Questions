def numOfPipes(input1):
    input2 = list(map(int , input().strip().split(" ")))
    for i in range(input1):
        for j in range(input1):
            if input2[i]<input2[j]:
                del input2[j]
    print(input2)
input1 = int(input())
numOfPipes(input1)