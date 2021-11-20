def  MaximunSubsegment(input1):
    list1 = []
    
    for i in range(input1):
        input2 = int(input()) 
        input3 =list(map(int , input().strip().split(" ")))[:input2]
        list1.append(input3)
    
    for list2 in list1:
        list3 = []
        for k in range(len(list2)):
            for l in range(len(list2)):
                
                if list2[k] < list2[l]:
                    list3.append(list2[l])
        print(list3)    

        
 
                




input1 = int(input())
MaximunSubsegment(input1)