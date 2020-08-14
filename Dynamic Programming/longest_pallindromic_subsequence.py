'''
https://leetcode.com/problems/longest-palindromic-subsequence/
Given a string s, find the longest palindromic subsequence's length in s. 
You may assume that the maximum length of s is 1000.
Example 1:
Input:
"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
 
Example 2:
Input:
"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
'''

# take second string as reverse of first string
# find LCS of string and its reversed string
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        s2 = s[::-1]
        
        l1 = len(s)
        l2 = len(s2)
        dp = [[0]*(l2+1) for _ in range(l1+1)]
        
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if s[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        return dp[l1][l2]