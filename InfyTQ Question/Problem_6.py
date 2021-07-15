String_final =''
string_input = input()
a = string_input.split(',')
for i in a:
    x,y = i.split(':')
    length = len(x)


    maximum = 0
    for j in y:
        if int(j) <= length and int(j) >= int(maximum):
            maximum = j

    if maximum == 0:
        String_final += 'X'
    else:
        string_input += x[int(maximum)-1]

print(String_final)        




