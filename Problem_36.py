'''

'''
def transmit(input1):
    for i in reversed(range(len(input1))):
        #for j in reversed(range(len(input1))):
            
            if input1[i] ==  input1[i-1]:
                print(input1[i])
                print(input1[i-1])
                print(input1[i])
              

input1 = input()
transmit(input1)