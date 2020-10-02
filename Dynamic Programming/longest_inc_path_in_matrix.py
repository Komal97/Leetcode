'''
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
Given an integer matrix, find the length of the longest increasing path.
From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:
Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:
Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
'''

# check in all 4 directions and maintain previous
class Solution:
    
    def lis(self, matrix, dp, r, c, prev):
        if r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix[0]) or matrix[r][c] <= prev or matrix[r][c] == -1:
            return 0

        if dp[r][c] != -1:
            return dp[r][c] 

        prev = matrix[r][c]
        matrix[r][c] = -1

        top = 1 + self.lis(matrix, dp, r-1, c, prev)
        bottom = 1 + self.lis(matrix, dp, r+1, c, prev)
        left = 1 + self.lis(matrix, dp, r, c-1, prev)
        right = 1 + self.lis(matrix, dp, r, c+1, prev)

        matrix[r][c] = prev
        dp[r][c] = max(top, bottom, left, right)
        return dp[r][c] 
    
    def longestIncreasingPath(self, matrix: List[List[int]]):
        
        if len(matrix) == 0:
            return 0
        elif len(matrix[0]) == 0:
            return 0
        n, m = len(matrix), len(matrix[0])
        
        dp = [[-1]*(m+1) for _ in range(n+1)]
        longestpath = 0
        for i in range(n):
            for j in range(m):
                path =  self.lis(matrix, dp, i, j, float('-inf'))
                longestpath = max(longestpath, path)
                
        return longestpath