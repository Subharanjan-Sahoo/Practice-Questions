'''

One programming language has the following keyword that cannot be used as identifiers:

'break','case','continue','default','defer','else','for','func','goto','range','return','struct','type','var'

write a program to find if the given word is a keyword or not.


'''
def KeyWord(input1):
    list1= ['break','case','continue','default','defer','else','for','func','goto','range','return','struct','type','var']
    if input1 in list1:
        print(input1 +' is a keyword') 
    else :
        print(input1 +' is not a keyword')


input1 = input("Enter the word: ")
KeyWord(input1)