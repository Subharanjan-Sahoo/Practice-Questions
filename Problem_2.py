# Most use Vowel in the String


def FindMostFrequentVowel(str):
    a=0
    e=0
    x=0 
    o=0 
    u=0
    for i in range(len(str)):
        if str[i] == "a" or str[i] == "A":
            a = a+1
        elif str[i] == "e" or str[i] == "E":
            e= e+1
        elif str[i] == "i" or str[i] == "I":
            x= x+1
        elif str[i] == "o" or str[i] == "O":
            o= o+1
        elif str[i] == "u" or str[i] == "u":
            u= u+1  
    if (a > e) and (a > x) and (a > o) and (a > u):
        print ('a')  
    elif (e > a) and (e > x) and (e > o) and (e > u):
        print ('e')
    elif (x > e) and (x > a) and (x > o) and (x > u):
        print ('i') 
    elif (o > e) and (o > x) and (o > a) and (o > u):
        print ('o')
    elif (u > e) and (u > x) and (u > o) and (u > a):
        print ('u')           

                 
str = input("Enter the String: ")
FindMostFrequentVowel(str)