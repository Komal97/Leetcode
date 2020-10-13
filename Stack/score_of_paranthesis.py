'''
https://leetcode.com/problems/score-of-parentheses/
Given a balanced parentheses string S, compute the score of the string based on the following rule:
() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 
Example 1:
Input: "()"
Output: 1

Example 2:
Input: "(())"
Output: 2

Example 3:
Input: "()()"
Output: 2

Example 4:
Input: "(()(()))"
Output: 6
'''

# if ( encounter, then append
# if ) then, if s.top is ( means it was previous element, so pop it, push score 1 in stack
# else pop from stack all scores, and sum them and push 2 * score
class Solution:
    def scoreOfParentheses(self, S: str):
        
        stack = []
        n = len(S)
        
        total = 0
        i = 0
        while i < n:
            
            if S[i] == '(':
                stack.append('(')
            else:
                if stack[-1] != '(':
                    c = 0
                    while len(stack) > 0 and stack[-1] != '(':
                        c += int(stack.pop())

                    stack.pop()
                    stack.append(str(2*c))
                else:
                    stack.pop()
                    stack.append('1')
            i += 1
                    
        while len(stack) > 0:
            total += int(stack.pop())
            
        return total
                    
# method - 2
# keep score till current depth
class Solution:
    def scoreOfParentheses(self, S: str):
        
        stack = [0]
        
        for s in S:
            if s == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2*v, 1)
        
        return stack.pop()
                
        
        
                    