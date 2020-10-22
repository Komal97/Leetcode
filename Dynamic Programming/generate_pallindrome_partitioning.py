'''
https://leetcode.com/problems/palindrome-partitioning/
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.
Example:
Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
'''

# use recursion to find all substrings
# store store result of pallindrome in dp
# initialize dp false, if extreme (s[idx] == s[i]) are equal and between them string is also pallindrome(check from dp) 
# then current string is also pallindrome
class Solution:
    def partition(self, s: str):
       
        def pallindromePartitioning(idx, output):
            
            if idx == n:
                ans.append(output)
                return

            for i in range(idx, n):
                # if extreme equal and either length is 2 or string between extreme is pallindrome
                if (s[idx] == s[i]) and (i-idx <= 2  or dp[idx+1][i-1]== True):
                    dp[idx][i] = True
                    pallindromePartitioning(i+1, output + [s[idx:i+1]]) 
                
        n, ans = len(s), []
        dp = [[False]*n for _ in range(n)]
        pallindromePartitioning(0, [])
        return ans