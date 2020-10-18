'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/#/description
Say you have an array for which the i-th element is the price of a given stock on day i. Design an algorithm to find the maximum profit. You may complete at most k transactions.
Note: You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:
Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:
Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
'''

# method - O(n^3)
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        n = len(prices)
        if k == 0 or n == 0:
            return 0
        
        dp = [[0]*(n) for _ in range(k+1)]
        
        for i in range(1, k+1):
            for j in range(1, n):
                maxval = dp[i][j-1]                     # if all transactions occured before current day
                
                for prev in range(j):                   # if j-1 transactions before current day, ans last transactions is between current day and jth 
                    maxval = max(maxval, prices[j] - prices[prev] + dp[i-1][prev])
                dp[i][j] = maxval                   
                
        return dp[k][n-1]

# method - O(n^2)
class Solution:
    
    def maxProfitInfinite(self, n, prices):
        summ = 0
        for i in range(1, n):
            if prices[i] >= prices[i-1]:
                summ += prices[i] - prices[i-1]
        return summ
        
    def maxProfit(self, k: int, prices: List[int]):
        
        n = len(prices)
        if n == 0 or k == 0:
            return 0
        
        # if k > n/2 means almost alternate transactions so it becomes infinite transaction problem
        if 2*k > n:                                             
            return self.maxProfitInfinite(n, prices)
            
        dp = [[0]*(n) for _ in range(k+1)]
        
        
        for i in range(1, k+1):
            maxdiff = float('-inf')     # keep max from prev row
            for j in range(1, n):
                maxdiff = max(maxdiff, dp[i-1][j-1] - prices[j-1])
                dp[i][j] = max(dp[i][j-1], maxdiff + prices[j])
               
        return dp[k][n-1]