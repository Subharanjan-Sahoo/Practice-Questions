'''
Given an array A[] of N integers and an integer X. The task is to count all the triplets (i, j, k) where 1 Si≤jsk≤N which satisfies the below

conditions.

1.XSj-i and X≤k-j.

2. A[i], A[j] and A[k] are odd.

Example 1:

Input:

N = 4

X = 1 A[] = {1, 2, 3, 3}

Output: 1

Explanation: There is only 1 triplet: (i=1, j-3, k-4) which satisfies all conditions.


'''

def oddTriplets(N,X):
    count = 0 
    A = list(map(int , input().strip().split(",")))[:N]
    for i in range(0 ,N):
        for j in range(i+1 ,N):
            for k in range(j+1 ,N):
                if(A[k] < A[i] and A[i] < A[j]):
                    count += 1

    print(count)            

    



N = int(input())
X = int(input())
oddTriplets(N,X)   