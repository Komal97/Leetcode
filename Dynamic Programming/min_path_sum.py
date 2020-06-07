'''
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

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        
        n = len(grid)
        m = len(grid[0])
        
        for i in range(n):
            for j in range(m):
                
                if i-1<0 and j-1<0:
                    continue
                elif j-1 < 0:
                    grid[i][j] += grid[i-1][j] 
                elif i-1 < 0:
                    grid[i][j] += grid[i][j-1]
                else:
                    grid[i][j] = min(grid[i][j] + grid[i][j-1], grid[i-1][j] + grid[i][j])
                    
        
        return grid[n-1][m-1]