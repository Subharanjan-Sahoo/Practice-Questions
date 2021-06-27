'''
Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Example 2:

Input: s = " "
Output: 0

'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        newstring =" "

        length = len(s)
        if length == 0 or s == " ":
            return 0
        else:
            for i in range(length-1,0,-1):
                if(s[i] == " "):
                    return len(newstring[::-1]) -1
                else:
                    newstring = newstring + s[i]
                        