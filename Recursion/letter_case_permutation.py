'''
https://leetcode.com/problems/letter-case-permutation/
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
'''

# at every step, we have 2 choices, each letter as capital or small and if digit then as it is include in output
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        
        def permutation(s, output, ans):
            if len(s) == 0:
                ans.append(output)
                return
            
            ch = s[0]
            if ch >= '0' and ch <= '9':
                permutation(s[1:], output + ch, ans)
            else:
                permutation(s[1:], output + ch.lower(), ans)
                permutation(s[1:], output + ch.upper(), ans)

        ans = []
        output = ''
        permutation(S, output, ans)
        return ans