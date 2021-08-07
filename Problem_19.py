def findnumber(A):
    N = A[0]
    X = A[1]
    K = A[2]
    S = list(input())[:N] 
    #Q = int(S)
    print(S)
    div1 = [S[i:i + X]for i in range(0, N, X)]
    print(div1[0])






A = list(map(int , input().strip().split( )))[:3]
findnumber(A)    