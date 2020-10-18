'''
https://leetcode.com/problems/search-a-2d-matrix/
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
Output: true
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
Output: false
'''

# O(log(mn))
# row = mid / totalcol (total items we have / col of 1 row gives on which row we are)
# col = mid % totalcol (works like a circular 1- D array)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int):
        
        if not matrix or target is None:
            return False
        
        row, col = len(matrix), len(matrix[0])
        
        low, high = 0, row*col-1
        
        while low <= high:
            mid = (low + high)//2
            num = matrix[mid//col][mid%col]
            
            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False