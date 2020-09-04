'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
Say you have an array for which the ith element is the price of a given stock on day i.
Find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:
Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
'''

class Solution:
    def maxProfit(self, prices: List[int]):
        
        n = len(prices)
        
        if n == 0:
            return 0
        
        # state series -> buy sell cooldown buy sell
        buy = -prices[0]                                # store buy current day on prv cooldown
        sold = 0                                        # store sold current day on prv buy
        cooldown = 0                                    # store cooldown current day on prv sold
        
        for i in range(1, n):
            nbuy = max(buy, cooldown-prices[i])
            nsold = max(sold, buy+prices[i])
            ncooldown = max(cooldown, sold)
            buy = nbuy
            sold = nsold
            cooldown = ncooldown
        
        return sold
            