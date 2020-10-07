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

# method - 1 => use stack , O(m+n) space
class Solution:
    def backspaceCompare(self, S: str, T: str):
        
        stack = []
        
        for s in S:
            if s == '#':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(s)
        
        s1 = ''.join(stack)
        
        stack = []
        
        for s in T:
            if s == '#':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(s)
        
        s2 = ''.join(stack)
        
        return s1 == s2

# start from last
class Solution:
    def backspaceCompare(self, S: str, T: str):
        
        
        i = len(S)-1
        j = len(T)-1
        skipS = 0
        skipT = 0
        
        while i >= 0 or j >= 0:
            
            # cancel out # from characters by keep count of # just like stack remove characters
            while i >= 0:
                if S[i] == '#':
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break
            
            while j >= 0:
                if T[j] == '#':
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break
            
            # if characters don't match
            if i >= 0 and j >= 0 and  S[i] != T[j]:
                return False
            # if any string finishes
            if (i >= 0 and j < 0) or (i < 0 and j >= 0):
                return False
            
            i -= 1
            j -= 1
        
        return True