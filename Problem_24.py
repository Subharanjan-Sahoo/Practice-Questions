def step(input1):
    c = 'R'
    x,y =0,0
    distance = 10

    for i in range(input1):
        if  c == 'R' :
            x = x + distance
            c = 'U'
            distance +=10
        elif c == 'U':
            y = y + distance
            c = 'L'
            distance +=10
        elif c == 'L':
            x = x-distance
            c = 'D'
            distance +=10
        elif c == 'D':
            y = y - distance
            c ='A'
            distance =distance+10
        elif c== 'A':
            x=x+distance
            c='R'
            distance =distance+10
    print(x,y)             
    

input1 = int(input())
step(input1)    