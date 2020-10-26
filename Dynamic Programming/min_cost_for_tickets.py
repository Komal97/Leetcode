'''
https://leetcode.com/problems/minimum-cost-for-tickets/
In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.
Train tickets are sold in 3 different ways:
a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.

Example 1:
Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total you spent $11 and covered all the days of your travel.

Example 2:
Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total you spent $17 and covered all the days of your travel.
'''

# recursion with memoization
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        
        def findmin(idx, day):

            if day > 365 or idx == len(days) or day > days[len(days)-1]:
                return 0
            
            if dp[day] != -1:
                return dp[day]
            
            if day < days[idx]:
                dp[day] = findmin(idx, day+1)
                return dp[day]
            
            val1 = costs[0] + findmin(idx+1, day+1)
            val2 = costs[1] + findmin(idx+1, day+7)
            val3 = costs[2] + findmin(idx+1, day+30)
            
            dp[day] = min(val1, val2, val3)
            return dp[day]
        
        dp = [-1]*(366)
        ans = findmin(0, 1)
        return ans
    
# tabular
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]):
        
        n = len(days)
        dp = [0]*(366)
        
        j = 1
        for i in range(n):
            
            # when day is not travel day, means amount remains same as prev travel day
            while j <= days[i]:
                dp[j] = dp[j-1]
                j += 1

            # travel ends today if i buy ticket 1 day ago
            val1 = costs[0] + dp[days[i]-1] 
            
            # travel ends today if i buy ticket 7 days ago (no need to travel all 7 days before)
            val2 = costs[1] + (dp[days[i]-7] if days[i]-7 >= 0 else 0)
            
            # travel ends today if i buy ticket 30 days ago (no need to travel all 30 days before)
            val3 = costs[2] + (dp[days[i]-30] if days[i]-30 >= 0 else 0)
            
            # find min of 3 options
            dp[days[i]] = min(val1, val2, val3)
        
        #print(dp[:30])
        return dp[days[n-1]]