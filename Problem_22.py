'''
Here you are given unbiased dice containing 6 faces. You will be given an output sum which should be obtained by throwing two dice. You need to return the number of all possibilities where the sum on both the dice is equal to the output sum. If there are no possibilities return 0.

Input

10

Output

3
'''
def dice(input1):
    count = 0
    for i in range(1,7):
        for j in range(1,7):
            if i + j == input1 :
                count = count + 1
    print(count)    

input1 = int(input())
dice(input1)  