'''
https://leetcode.com/problems/minimum-path-sum/
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''

# recursive
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        def findCost(grid, i, j, m, n):
            
            if i >= m or j >= n:
                 return float('inf')
            
            if i == m-1 and j == n - 1:
                return grid[i][j]
            
            
            val1 = grid[i][j] + findCost(grid, i+1, j, m, n)
            val2 = grid[i][j] + findCost(grid, i, j+1, m, n)
            return min(val1, val2)
    
        return findCost(grid, 0, 0, len(grid), len(grid[0]))
    
# tabulation
# if start from 0,0 => at a position, one can come from top or left
# if start from m,n => from a position, one can go to down or right 
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    grid[i][j] += grid[i][j-1] 
                elif j == 0:
                    grid[i][j] += grid[i-1][j] 
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                    
        return grid[m-1][n-1]
