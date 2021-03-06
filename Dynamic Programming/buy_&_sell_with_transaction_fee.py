'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/
Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.
You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)
Return the maximum profit you can make.
Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
'''

class Solution:
    def maxProfit(self, prices: List[int], fee: int):
        
        n = len(prices)
        buy = -prices[0]                                        # stores value with extra stock
        sold = 0                                                # stores max profit till now (bsbs)
        
        for i in range(1, n):
            nbuy = max(buy, sold-prices[i])                     # max(prv day buy or buy today) 
                                                                # (sold-prices[i]) means buy on prv sold
            nsold = max(sold, buy+prices[i]-fee)                # max(prv day sell or sell today)
                                                                # (buy+prices[i]-fee) means sell on prv buy with transaction fee
            buy = nbuy
            sold = nsold
            
        return sold