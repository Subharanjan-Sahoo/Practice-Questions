'''
We a Program TO fed SUM of ALL integers BETWEEN Iwo integer nubers takas ut AND are divisible BY 7.

Input1 < input2

Example input:

1 20

Example Output:

21

'''
def divisible(x):
    input1 = x[0]
    input2 = x[1]
    sum = 0
    for i in range(input1,input2+1):
        #print(i)
        if i % 7 == 0:
            sum += i
    print(sum)



x = list(map(int, input().strip().split(" ")))
divisible(x)