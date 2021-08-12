'''
input = Welcome to mettl
output = mettl to Welcome
 
'''

def reverse(input1):
    word = []
    word = input1.split(" ")
    reverseno = word[len(word)::-1]
    tostr = " "
    tostr =' '.join(reverseno)
    print(tostr)

input1 = input()
reverse(input1)