'''

Given an array of size n .write a function to rearrange the numbers of array 
in such way that even and odd numbers are arranged altematively in increasing order.

Example:
input1= 5
input2= {9,12,23,6,5}

OUTPUT= {5,8,9,12,23}

'''

def evenodd(list1,l3):

    list1.sort()
    n = 0
    l1=list()
    l2= list() 
    l3 =list ()
    for i in range(len(list1)):
        if (list1[i] % 2 == 0) :
            l1.append(list1[i])
        else:
            l2.append(list1[i])
             
    index = 0
    i = 0
    j = 0
    flag = False
    if (list1[0] % 2 == 0):
        flag = True
    while (index < n):
        if (flag == True):
            list1[index] = l1[i]
            l3.append(l1(i))
            index +=1
            i +=1
            flag = ~flag
        else:
            list1[index] = l2[j]
            l3.append(l2(j))
            index += 1
            j += 1
            flag = ~flag 
        return l3    

    for i in range(n):
        print(list1[i],end = " ")     
          
n = int(input("Enter the number of list in array: "))
list1 = [int(input("Enter the number: ")) for i in range(n)]




evenodd(list1)


