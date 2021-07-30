'''

Description: As a young jedi you must learn to converse with Yoda. You have found a simple rule that helps change a "normal" sentence into "Yoda talk". 
Take the first two words in the sentence and place them at the end. Write a program that uses this rule to change normal sentence into "Yoda talk".

Input:

Input consists of a string that you must change

into "Yoda talk". Assume that the maximum length of the string is 100:

Output:

Print the corresponding sentence in Yoda talk.

Sample Input:

I will go now to find the Wookiee

Sample Output:

go now to find the Wookiee I will

'''

def yoda(input1):
    str = " "
    temp = input1.split(" ")
    temp2 = temp[:2]
    temp3 = temp[2:]
    convert = temp3 + temp2

    print(str.join(convert))

input1 = input("Enter the string: ")
yoda(input1)