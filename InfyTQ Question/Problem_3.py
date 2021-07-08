def oddplace(num):
    oddplacenum = ""
    nos = str(num) 
    for i in range(1,len(nos)):
        if (i % 2 != 0):

            oddplacenum += str(int(nos[i])**2) 
    print(oddplacenum[:4])   





num = int(input("Enter the number: "))
oddplace(num)