'''
Same as qustion number - 9

'''

def magic(temp,input2):
    sumChange = 0
    sumNoChange = 0
    for i in range(len(input2)):
        for j in range(i+1,len(input2)):
            if input2[i] > input2[j]:
                input2[i],input2[j] = input2[j],input2[i]
    for k in range(len(input2)):
        if input2[k] == temp[k]:
            sumChange = input2[k]+ sumChange
        else :
            sumNoChange = input2[k] + sumNoChange
    print(sumChange - sumNoChange)             
   




input1 = int(input())
input2 = list(map(int , input().strip().split(" ")))[:input1]
temp = input2[:]
magic(temp,input2)