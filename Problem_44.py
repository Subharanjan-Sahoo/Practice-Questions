'''
Problem Statement and casesProblem DescriptionA chocolate factory is packing chocolates into the packets.
The chocolate packets here represent an array arrt of Nnumber of integer values. 
The task is to find the empty packets(0) of chocolate and push it to the end of the conveyorbelt(array).
For Example: N=7 and arr=[4,5,0,1.9,c ]).
There are 3 empty packets in the given set. 
These 3 empty packets representedas O should be pushed towards the end of 
the arrayInputOutput7- Value of N4519500[4,5,0,1,0,0,5]Element of arr[O] to arr[N-1],
While input each element is separated by newlineInputOutput6- Value of N618200[6,0,1,8,0,2]Element of arr[0] to arr[N While input each element is separated by newline

'''
def cololate(input1):
    zero = []
    num = []
    ans = " "
    arr1 = list(map(int , input().strip().split(",")))[:input1]
    for i in range(len(arr1)):
        if arr1[i] == 0:
            zero.append(arr1[i])
        else:
            num.append(arr1[i])
    sum = num+zero
    ans = ' '.join(map(str, sum))
    print(ans)
            
    



input1 = int(input())
cololate(input1)