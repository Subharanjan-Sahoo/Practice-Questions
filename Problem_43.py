'''
A high-profile secret agency wants to handle all the messages sent and received in ciphers. They need to build a program/software where every mail sent or received in the organization will be encrypted using some secret codes. One of formats used can be as follows:

Actual

Cipher

9

h

m

Actual

m

P

Cipher

P

V

Actuals

Cipher x

W

b

2

d

e

The task is to encrypt the given string(str1) as per the ciphers given in the format above. Note: String cannot have any special characters, space, number or any uppercase latter.


'''



def Secret(str1):
    new = ""
    for i in range(len(str1)):
        if ord(str1[i]) <= ord("v"):
            new += chr(ord(str1[i])+5)
        else:
            new += chr(ord(str1[i])-ord('v')+ord('a'))
    print(new)          



str1 = input()
Secret(str1)