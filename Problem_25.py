def Profit(input1):
    sum = 1
    nums = list(map(int , input().strip().split(" ")))[:input1]
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] < nums[j]:
                if 2*nums[i] == nums[j]:
                     sum  = sum + nums[j]
                     print(sum)
    print(sum)                   


input1 = int(input())
Profit(input1)