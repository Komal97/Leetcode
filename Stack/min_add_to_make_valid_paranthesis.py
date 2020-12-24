'''
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.
Formally, a parentheses string is valid if and only if:
It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

Example 1:
Input: "())"
Output: 1

Example 2:
Input: "((("
Output: 3

Example 3:
Input: "()"
Output: 0

Example 4:
Input: "()))(("
Output: 4
'''

# method-1 => maintain opening and closing stack keeping unbalanced paranthesis
class Solution:
    def minAddToMakeValid(self, S: str):
        
        opening = []
        closing = []
        
        for ch in S:
            if ch == '(':
                opening.append(ch)
            else:
                if len(opening) > 0:
                    opening.pop()
                else:
                    closing.append(ch)
        
        return len(opening) + len(closing)

# method-2 => maintain opening and closing count
class Solution:
    def minAddToMakeValid(self, S: str):
        
        opening = 0
        closing = 0
        
        for ch in S:
            if ch == '(':
                opening += 1
            else:
                if opening > 0:
                    opening -= 1
                else:
                    closing += 1
        
        return opening + closing