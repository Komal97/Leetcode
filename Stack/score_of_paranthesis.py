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
    def scoreOfParentheses(self, s: str) -> int:
        
        st = []
    
        for ch in s:
            if ch == '(':
                st.append(ch)
            else:
                if st[-1] == '(':
                    st.pop()
                    st.append('1')
                else:
                    n = 0
                    while len(st) > 0 and st[-1] != '(':
                        n += int(st.pop())
                    st.pop()
                    st.append(str(2*n))
        total = 0
        while len(st) > 0:
            total += int(st.pop())
        
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
                
        
        
                    