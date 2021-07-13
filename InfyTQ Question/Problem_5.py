string = input()
stack = []
Counter = 0 
for a in string:
    if (a == '[' or a == '{' or a =='('):
        stack.append(a)
        Counter += 1
        continue


    if(len(stack) == 0):
        print(Counter+1)
        exit()


    b = stack.pop()

    if(a == ']' and b == '['):
        Counter +=1
    elif(a == '}' and b == '{'):
        Counter += 1
    elif(a == ')' and b == '('):
        Counter +=1

if(len(stack)==0):
    print(0)
else:
    print(Counter+1)                     