def jumbled(input1):
    list1 = []
    list2 = []
    list3 = []
    for i in range(input1):
        P = input()
        S = input()
        list1.append(P)
        list2.append(S)
    for j in range(len(list1)):
        for k in range(len(list2)):
            if j == k:
                for l in list2[j]:
                    list3.append(list1.find(l))
                list1.sort()
                for l in list1:
                    print(list1[l],end='')

input1 = int(input())
jumbled(input1)