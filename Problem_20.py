def Friends(input1):
    num = []
    binary1 = []
    sum = 0
    for i in range(0,input1):
        num1 = int(input())
        num.append(num1)
   # for j in range(0,input1):           |
    #    binary = bin(num[j])            |                  Convert to binary number 
    #    binary1.append(binary)          |
          
    #for k in range(0,input1):           |
        #print(binary)                   |                  Binary Addtion
    #    sum = sum + int(binary1[i],2)   | 
     #   print("Sum:",sum)               |
    for l in range(0,input1):
        sum = sum + num[l]
        
        print(sum)      




input1 =int(input())
Friends(input1)