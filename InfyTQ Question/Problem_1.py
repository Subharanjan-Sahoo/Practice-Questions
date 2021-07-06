def str1(allno):
    index_of_4 = allno.index('4')
    index_of_7 = allno.index('7')
    
    num1 = 0
    num2 = ""

    for i in range(0,len(allno)):
        if(i<index_of_4 or i>index_of_7):
            num1 += int(allno[i])
    print(num1)        
    for i in range(index_of_4,index_of_7 + 1):
        num2 += allno[i]
    print(num2)            
    print(num1+int(num2))    



    
allno = input("Enter the all string : ").split(",")
str1(allno)