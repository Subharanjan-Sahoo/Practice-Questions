list1 = []
list2 = []
def consecutivePrimeNo(input1):
    for i in range(2,input1):
        if prime(i) == True:
            list1.append(i)

'''
for k in range(len(list1)):
    for l in range(k+1,len(list1)):
        sum = list1[k] + list1[l]
        if sum in list1:
            list2.append(sum)
'''        

def prime(i):      
    for j in range(2,i):
        if i % j == 0:
            return False
    return True  




input1 = int(input())
consecutivePrimeNo(input1)
print(list1)