'''
Sample Input
3
3000 
5000
4000
2
5
3

Sample Output
12500.0

'''
def Employee(N):
    A = []
    B = [] 
    for i in range(N):
        S = int(input())
        A.append(S)
    for j in range(N):
         Y = int(input())
         B.append(Y)
    for k in range(N):
        if B[k] > 4:
            A[k] = A[k] + A[k]*0.1
    print(sum(A))    
    
            



N = int(input())


Employee(N)
