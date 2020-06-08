'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:
Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
'''
class Solution:
# method 1 -> using extra space
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        row = [0]*r
        col = [0]*c
        
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1
        
        for i in range(r):
            for j in range(c):
                if row[i] == 1 or col[j] == 1:
                    matrix[i][j] = 0
                   
# method 2 -> without using extra space
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        row = False
        col = False
        
        for i in range(r):
            for j in range(c):
                if i == 0 and matrix[i][j] == 0:
                    row = True
                if j == 0 and matrix[i][j] == 0:
                    col = True
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
              
        
        for i in range(1, r):
            for j in range(1, c):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
                    
        if row:
            for i in range(c):
                matrix[0][i] = 0
        if col:
            for i in range(r):
                matrix[i][0] = 0
                    