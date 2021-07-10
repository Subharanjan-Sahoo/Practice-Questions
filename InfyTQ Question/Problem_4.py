import re
def largestevenno(evenno):
    for i in set(evenno):
        digits = 0
        if i.isdigit():
           digits += evenno[i]
           digits.sort()
           digits.reverse()
           Number =int(''.join(digits))
           if Number % 2 == 0:
               print(Number)
           else:
               length =len(digits)
               for i in range(length-1,0,-1):
                   if int(digits[i]) % 2 == 0:
                        a = digits[i]
                        digits.remove(a)
                        digits.insert(length-1,a)
                        even = int("".join(digits))
                        print(even)



evenno = input("Enter the even number: ")
largestevenno(evenno) 
