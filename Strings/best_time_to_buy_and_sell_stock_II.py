'''
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

class Solution:

# method - 1
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        
        if n == 0:
            return 0
        
        buy  = [0 for _ in range(n)]
        sell  = [0 for _ in range(n)]
        
        buy[0] = prices[0]
        for i in range(1, n):
            if prices[i] < buy[i-1]:
                buy[i] = prices[i]
            else:
                buy[i] = prices[i-1]
           
        sell[n-1] = prices[n-1]
        for i in range(n-2, -1, -1):
            if prices[i] > sell[i+1]:
                sell[i] = prices[i]
            else:
                sell[i] = sell[i+1]
                
        profit = 0
        
        for i in range(n):
            if sell[i] - buy[i] > profit:
                profit = (sell[i] - buy[i])
        
        return profit
		
# method - 2  (Kadane's Algorithm)
	def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        
        if n == 0:
            return 0
        
        profit = 0
        curr_sum = 0
        
        for i in range(1, n):
            curr_sum = curr_sum + (prices[i] - prices[i-1])
            
            profit = max(profit, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
           
        return profit
        