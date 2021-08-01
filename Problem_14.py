def numdiv(input1):
    First = []
    Second = []
    input2 = list(map(int, input("Enter the Elements: ").strip().split(",")))[:input1]
    input3 = int(input("Enter the number: "))
    First = input2[:input3]
    Second = input2[input3:]
    
    Combine = Second + First
    print(Combine)


input1 = int(input("Enter the no of elements: "))
numdiv(input1)   