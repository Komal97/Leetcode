'''
https://leetcode.com/problems/number-of-islands/
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''

# variation of connected components
# each cell denoted each vertex, and from each vertex we can move in all 4 directions
# so from each cell, call countIslands
class Solution:
    
    def countIslands(self, grid, i, j):
        
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
            return
        
        grid[i][j] = '0'
        self.countIslands(grid, i+1, j)
        self.countIslands(grid, i-1, j)
        self.countIslands(grid, i, j+1)
        self.countIslands(grid, i, j-1)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        
        n = len(grid)
        
        if n == 0:
            return 0
        
        m = len(grid[0])
        
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    self.countIslands(grid, i, j)
                    count += 1
        return count