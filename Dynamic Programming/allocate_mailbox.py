'''
https://leetcode.com/problems/allocate-mailboxes/
Given the array houses and an integer k. where houses[i] is the location of the ith house along a street, your task is to allocate k mailboxes in the street.
Return the minimum total distance between each house and its nearest mailbox.
The answer is guaranteed to fit in a 32-bit signed integer.

Example 1:
Input: houses = [1,4,8,10,20], k = 3
Output: 5
Explanation: Allocate mailboxes in position 3, 9 and 20.
Minimum total distance from each houses to nearest mailboxes is |3-1| + |4-3| + |9-8| + |10-9| + |20-20| = 5 

Example 2:
Input: houses = [2,3,5,12,18], k = 2
Output: 9
Explanation: Allocate mailboxes in position 3 and 14.
Minimum total distance from each houses to nearest mailboxes is |2-3| + |3-3| + |5-3| + |12-14| + |18-14| = 9.

Example 3:
Input: houses = [7,4,6,1], k = 1
Output: 8

Example 4:
Input: houses = [3,6,14,10], k = 4
Output: 0
'''

class Solution:
    def minDistance(self, houses: List[int], k: int):
        
        n = len(houses)
        
        if n <= k:
            return 0
                                               
        def findMin(idx, k):
            
            # if reach end and all mailboxes are placed
            if idx == n and k == 0:
                return 0
            
            # if not reach end or mailbox are remaining then false case
            elif idx == n or k == 0:
                return float('inf')
            
            # if already found solution
            elif dp[idx][k] != -1:
                return dp[idx][k]
            
            ans = float('inf')
            # run through all choices of position of 1 mailbox and call for k-1 boxes
            for i in range(idx, n):  
                ans = min(ans, cost[idx][i] + findMin(i+1, k-1))
            
            dp[idx][k] = ans
            return ans
        
        max_val = max(houses)
        cost = [[0]*(n+1) for _ in range(n+1)]
        dp = [[-1]*(n+1) for _ in range(n+1)]
        
        # median works on sorted array so sort
        houses.sort()
        
        # i and j represents interval
        for i in range(n):
            for j in range(i, n):           
                # (i+j)/2 is median where mail box is placed so find total cost in current interval
                for x in range(i, j+1):
                    cost[i][j] += abs(houses[(i + j)//2] - houses[x])
        
        return findMin(0, k)