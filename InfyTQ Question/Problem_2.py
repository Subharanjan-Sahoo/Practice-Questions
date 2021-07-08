'''
Problem to reverse a string after removing dupecate characters

'''   

string = input("Enter the string: ")

out_string =" "

for i in string:
    if i not in out_string:
        out_string +=  i

a= out_string[::-1]
print(a)