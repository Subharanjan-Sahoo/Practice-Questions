'''
For a given positive number num, identify the palindrome formed by performing the following operations-

Add num and its reverse
Check whether the sum is palindrome or not. If not, add the sum and its reverse and repeat the process until a palindrome is obtained

For example:

If original integer is 195, we get 9,339, as the resulting palindrome after the fourth addition:


Input format: Read num from the standard input stream.

Output format: Print the palindrome calculated to the standard output stream.


Example 1

Sample input:

124

Sample output:

545

'''

def palindrome(num):
    sum = int(num) +int(num[::-1]) 
    sum = str(sum)
    if (sum == sum[::-1]):
        return sum
    else:
        return palindrome(sum)    
   




num = input("Enter the number: ")
print(palindrome(num))