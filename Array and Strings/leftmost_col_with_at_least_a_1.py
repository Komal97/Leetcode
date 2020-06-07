'''
A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.
Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.
You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:
BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the matrix is n * m.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

Example 1:
Input: mat = [[0,0],[1,1]]
Output: 0

Example 2:
Input: mat = [[0,0],[0,1]]
Output: 1

Example 3:
Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
Output: 1
'''

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
# method - 1 --> use binary search  (O r*log c)
	def find_firstOne(self, binaryMatrix, row, col_count):
        start = 0
        end = col_count - 1
        ans = -1
        
        while(start <= end):
            mid = int((start + end)/2)

            if binaryMatrix.get(row, mid) == 1:
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        return ans
                    
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        dimen = binaryMatrix.dimensions()
        n = dimen[0]
        m = dimen[1]
        min_ans = m
        
        for row in range(n):
            ans = self.find_firstOne(binaryMatrix, row, m)
            if ans > -1:
                min_ans = min(min_ans, ans)
        if min_ans == m:
            return -1
        
        return min_ans
		
# method - 2 --> start from right top, if 1 then move left, if 0 then down(O r + c)
	def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        dimen = binaryMatrix.dimensions()
        n = dimen[0]
        m = dimen[1]
        row = 0
        col = m-1
        ans = -1
        
        while(row < n and col >= 0):
            if binaryMatrix.get(row,col) == 1:
                ans = col
                col -= 1
                
            else:
                row += 1
        
        return ans