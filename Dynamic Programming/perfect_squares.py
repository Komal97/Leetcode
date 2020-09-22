'''
https://leetcode.com/problems/perfect-squares/
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''

# similar to min coin change
from math import sqrt
class Solution:
    
    def numSquares(self, n: int):
        
        maxel = n+1
        dp = [maxel]*(n+1)
        dp[0] = 0
        x = int(sqrt(n)) + 1
        for i in range(1, x+1):                             # similar to coins
            for j in range(i*i, n+1):                       # similar to amount
                val = dp[j-(i*i)]
                if val != maxel:
                    dp[j] = min(dp[j], val+1)
    
        return dp[n] if dp != maxel else -1