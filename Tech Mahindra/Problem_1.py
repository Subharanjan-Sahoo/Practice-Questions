'''

Write a program to calculate the total bill tax amount for a list of bill tax amounts passed as an array of long integers


Up to the 1000, there is no tax applicable,subsequently , a flat tax of 10% is applicable for remaining amount as per the tax rate.



input1:5

input2:1000 2000 3000 4000 5000


Output : 1000

'''

def calcTotalTax(input1):
    input2= []
    sum = 0
    sumpercent = 1
    input2 = list(map(int, input("Enter the number of Element: ").strip().split(" ")))[:input1]
    for i in range(input1):
        if input2[i] > 1000:
            sum = sum + input2[i]
    print(sum)        
    sumpercent = 0.1*sum
    sumpercent = int(sumpercent)
    print(sumpercent)




input1 = int(input("Enter the of Element: "))
calcTotalTax(input1) 