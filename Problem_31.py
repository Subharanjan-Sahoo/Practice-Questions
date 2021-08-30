def singlefile(input1):
    reminder = []
    rev = " "
    for i in range(5):
        if input1 / 5 != 0:
            reminder.append(int(input1 % 5))
            input1 = input1 / 5
        rev = ((reminder)[::-1])
    for i in rev:
        print(i, end="")



input1 = int(input())
singlefile(input1)