'''
https://leetcode.com/problems/generate-parentheses/
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

# append open bracket and keep its count
# append closing bracket and keep its count
# open count < n and close count < n
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def generate(l, r, output):
            if l == r and l == n:
                ans.append(output)
                return
            
            if l < n:
                generate(l+1, r, output + '(')
            if r < l:
                generate(l, r+1, output + ')')
        
        ans = []
        generate(0, 0, '')
        return ans