# You have given an array of integers a and an integer k. 
# Your task to calculate the number of way to pick two diffrerent indices i < j,
# such that a[i]+ a[j] is divisible by k.


def sumDivisibleBy(a ,k):
    num = 0
    sum = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if i < j:
                sum = a[i] + a[j]
                    #print(a[i], a[j])
                    #print(sum)
                if (sum % k == 0):
                   num = num +1
    print(num)

s = sumDivisibleBy([1, 2, 3, 4, 5],3)
#print(sumDivisibleBy(a ,k))

