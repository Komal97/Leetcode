'''
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
'''

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        stack = ""
        for i in range(len(S)):
            if S[i] != "#":
                stack = stack + S[i]
            else:
                if len(stack)>0:
                    stack = stack[:-1]
        
        print(S)
        
        stack = ""
        for i in range(len(T)):
            if T[i] != "#":
                stack = stack + T[i]
            else:
                if len(stack)>0:
                    stack = stack[:-1]
        print(T)
        
        if S==T:
            return True
        else:
            return False