"Revese the List"
"-----------------------Using slice Oparater---------------"

def revese(input1):
    input2 = list(map(int, input().strip().split(" ")))[:input1]
    temp = input2[::-1]
    print(temp)


input1 = int(input())
revese(input1)      



"------------------------Using For loop----------------------"
def revese(input1):
    list1 = []
    input2 = list(map(int , input().strip().split(" ")))[:input1]
    print(input2)
    for i in range(input1-1,-1,-1):
        list1.append(input2[i])
    print(list1)    
    

input1 = int(input())
revese(input1)

