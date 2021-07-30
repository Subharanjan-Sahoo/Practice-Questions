'''

Reverse digits

Reverse(D) to be the reversal of all digits in D.

For example, Reverse(349)=943, Reverse(93)=39, and Reverse(340) = 43. Amrit wants to go to the movies with Nayak on some day D satisfying psDsq, but he knows

he only goes to the movies on days he considers to be lucky, Nayak considers a day to be lucky if the absolute value of the difference between d and Reverse(d) is evenly divisible by s. Given p, q, and s, count and print the number of lucky days when Amrit and Nayak can go to

the movies.

Input Format

A single line of three space-separated integers describing the respective values of p, q, and s

Constraints.

1p,s.q 10000

Output Format Print the number of beautiful days in the inclusive range between p and q.

Sample Input

10 13 6

Sample Output

2

'''
def diffrence(input1):
    p= input1[0]
    q= input1[1]
    s= input1[2]
    rev =[]
    notrev = []
    str1 =" "
    luckday = 0
    for i in range(p , q+1):
        notrev.append(i)
        str1 = str(i)
        rev.append(str1[::-1])
    for j in range(len(rev)): 
        if (notrev[j] - int(rev[j])) %  s == 0:
            luckday = luckday + 1
    print(luckday)        
        
        #print("rev",rev)
        #print("notrev",notrev)
        





input1 = list(map(int, input("Enter the numbers: ").strip().split(" ")))
diffrence(input1)