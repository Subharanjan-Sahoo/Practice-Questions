def PrimeNo(n):
    count = 0
    k = 0
    if n > 1:
        for j in range(1,n+1):
            if (n % j) == 0:
                k=k+1
            else:
                count = count+1 
        print(count)
            
    
n =int(input("Enter the Number: "))
s = PrimeNo(n)