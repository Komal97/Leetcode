'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/#/description
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.
Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''

# method - 1
# find min from left to right
# find max from right to left
# find diff b/w them and max diff is max profit
class Solution:
    def maxProfit(self, prices: List[int]):
        n = len(prices)
        min_price = [0]*n
        min_price[0] = price[0]
        for i in range(1, n):
            min_price[i] = min(min_price[i-1], price[i])

        max_profit = 0
        max_price = float('-inf')
        for i in range(n-1, -1, -1):
            max_price = max(max_price, price[i])
            max_profit = max(max_profit, abs(max_price - min_price[i]))
        
        return max_profit

# method - 2
# consider current day as selling day and find max profit 
# to maximize current profit, buying should be minimum so keep minimum from days before current day
class Solution:
    def maxProfit(self, prices: List[int]):
        
        n = len(prices)
        min_buy_val = float('inf')
        max_profit = 0
        for i in range(n):
            min_buy_val = min(min_buy_val, prices[i])
            max_profit = max(max_profit, abs(min_buy_val-prices[i]))
            
        return max_profit