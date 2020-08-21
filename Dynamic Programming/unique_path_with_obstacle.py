'''
https://leetcode.com/problems/unique-paths-ii/submissions/
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.
Example 1:
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
'''

# in base case - set obstacleGrid[0][0] and obstacleGrid[n-1][m-1] for 1 and 0 (both conditions)
# if obstacleGrid[i][j] = 1, means current cell is obstacle so obstacleGrid[i][j] = 0
# else obstacleGrid[i][j] = down value + right value
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]):
        
        if obstacleGrid[0][0] == 1:
            return 0
        
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        
        if obstacleGrid[n-1][m-1] == 1:             # if blocked
            obstacleGrid[n-1][m-1] = 0              # number of paths become 0
        else:
            obstacleGrid[n-1][m-1] = 1              # else number of paths become 1
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if i == n-1 and j == m-1:
                    continue
                if obstacleGrid[i][j] == 1:         # if blocked
                    obstacleGrid[i][j] = 0
                else:
                    val1 = obstacleGrid[i][j+1] if (j+1 < m) else 0
                    val2 = obstacleGrid[i+1][j] if (i+1 < n) else 0
                    obstacleGrid[i][j] = val1 + val2
                
        return obstacleGrid[0][0]
        