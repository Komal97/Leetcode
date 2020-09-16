'''
https://leetcode.com/problems/wildcard-matching/
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Example 1:
Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

Example 2:
Input:
s = "acdcb"
p = "a*c?b"
Output: false
'''

# recursion + memoized
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        dp = [[-1]*(len(s)+1) for _ in range(len(p)+1)]
        
        def wildCard(p, i, s, j):
            if i == len(p) and j == len(s):
                return True
            elif i == len(p) and j < len(s):
                return False
            elif j == len(s):                                   # if string, finish and pattern has * left 
                for k in range(i, len(p)):
                    if p[k] != '*':
                        return False
                return True
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            elif p[i] == s[j] or p[i] == '?':                   # char match or ? -> i++, j ++
                val1 = wildCard(p, i+1, s, j+1)
                dp[i][j] = val1
                if val1:
                    return True
            elif p[i] == '*':                       
                val2 = wildCard(p, i+1, s, j+1)                 # if * become 1 char-> i++, j++
                dp[i][j] = val2
                if val2:
                    return True
                val3 = wildCard(p, i, s, j+1)                   # if * become 1 char-> i, j++
                dp[i][j] = val3
                if val3:
                    return True
                val4 = wildCard(p, i+1, s, j)                   # if * become empty-> i++, j
                dp[i][j] = val4
                if val4:
                    return True
            return False
        
        return wildCard(p, 0, s, 0)

# tabulation
class Solution:
    def isMatch(self, s: str, p: str):
        
        n = len(s)
        m = len(p)
        
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[m][n] = True                                         # 2 empty char are same
        
        for i in range(m-1, -1, -1):
            for j in range(n, -1, -1):
                if j == n:                                      # if str is empty and pattern has *        
                    if p[i] == '*':                             # check further pattern matches or not
                        dp[i][j] = dp[i+1][j]
                    else:
                        continue
                elif p[i] == s[j] or p[i] == '?':               # char match or ?, check further string is matched
                    dp[i][j] = dp[i+1][j+1]
                elif p[i] == '*':                               # if * becomes empty then i+1, j
                    dp[i][j] = dp[i+1][j] or dp[i][j+1]         # else check i, j+1
                
        
        return dp[0][0]