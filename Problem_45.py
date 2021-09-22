'''
Problem Description

An English school teacher is teaching how to build sentences for kindergarten students. She starts by teaching two words in a sentence, then 3 words and so on. The next step is that she asks the students to find which word in the sentence they have made has the maximum number of alphabets. The task here is to write program to find the longest word in each input sentence(str). Note: The sentence can consist of uppercase, lowercase alphabets, special characters and numbers.

Input

Knowledge is the greatest gift

Output

Explanation

we can derive the word with highest number of characters is knowledge. Hence, output is 9.

Input

Output

11223##%U66778899 Saturn V rocket's first stage carries 203,400 gallons (770,000 litres) of kerosene fuel

19

Explanation

Longest word in the sentence is 11223##%U66778899 Hence, output is 19.


'''
def longenglish(input1):
    list1=[]
    list1 = input1.strip().split(" ")
    temp1 = 0
    length = []
    for i in range(len(list1)):
        temp = len(list1[i])
        length.append(temp)
    for j in range(len(length)):
        if temp1 < length[j]:
            temp1 = length[j]
    print(temp1)        



input1 = input()
longenglish(input1)