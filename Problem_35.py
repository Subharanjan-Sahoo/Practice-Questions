'''
                                       FIZZ   AND    BUZZ         
'''


start = int(input())
end = int(input())
nums = []
for i in range(start,end+1):
    nums.append(i)
for j in range(len(nums)):
    if nums[j] % 3 == 0:
        print("Fizz")
    elif nums[j] %5 == 0:
        print("Buzz")
    else:
        print(nums[j])         
