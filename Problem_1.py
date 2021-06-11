 #  You need to write a Program to find the total number of "UPPERCASE" characters in a given string.


def uppercase(str1):
    j = 0
    for i in range(len(str1)):
        if str1[i]>= 'A' and str1[i] <= 'Z':
            j = j+1
    print(j)

str1 = input("Enter the String: ")
uppercase(str1)


