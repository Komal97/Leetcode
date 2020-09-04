'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
Example 1:
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''
class Solution:
    def maxProfit(self, prices: List[int]):
        
        # start from ind 0 and maintain max profit if sell today
        n = len(prices)
        sell_profit = [0]*n
        min_val = prices[0]
        for i in range(1, n):
            min_val = min(min_val, prices[i])
            max_profit = max(sell_profit[i-1], prices[i]-min_val)
            sell_profit[i] = max_profit
        
        # start from ind n-1 and maintain max profit if buy today and sell later
        total_profit = 0
        buy_profit = [0]*n
        max_val = prices[n-1]
        for i in range(n-2, -1, -1):
            max_val = max(max_val, prices[i])
            max_profit = max(buy_profit[i+1], max_val - prices[i])
            buy_profit[i] = max_profit
            
            # at index, we store 2 values, if buy earlier & sell today and if buy today & sell later
            total_profit = max(total_profit, sell_profit[i] + buy_profit[i])

        # return max of sum of 2 values
        return total_profit