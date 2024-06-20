'''
https://leetcode.com/problems/find-a-peak-element-ii/description/
A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.
Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].
You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.
You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.

Example 1:
Input: mat = [[1,4],[3,2]]
Output: [0,1]
Explanation: Both 3 and 4 are peak elements so [1,0] and [0,1] are both acceptable answers.

Example 2:
Input: mat = [[10,20,15],[21,30,14],[7,16,32]]
Output: [1,1]
Explanation: Both 30 and 32 are peak elements so [1,1] and [2,2] are both acceptable answers.
'''

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        s = 0
        e = len(mat[0])-1

        while s <= e:
            mid_col = (s+e)//2
            max_row = 0
            for r in range(len(mat)):
                max_row = r if mat[r][mid_col] >= mat[max_row][mid_col] else max_row

            if mid_col+1<=e and mat[max_row][mid_col] < mat[max_row][mid_col+1]:
                s = mid_col + 1
            elif mid_col-1 >= 0 and mat[max_row][mid_col] < mat[max_row][mid_col-1]:
                e = mid_col-1
            else:
                return [max_row, mid_col]
        
        return [-1, -1]