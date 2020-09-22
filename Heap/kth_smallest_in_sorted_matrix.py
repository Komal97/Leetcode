'''
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,
return 13.
'''

# method - 1 => use concept of merge k sorted array (push elements from each row)
# when pop, count+=1 and if count = k return number
# complexity - O(min(K,N)+K∗logN).
from heapq import heappush, heapreplace
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int):
        
        n = len(matrix)
        if n == 0:
            return 0
        
        heap = []
        for i in range(n):
            heappush(heap, [matrix[i][0], i, 0])
        
        count = number = 0
        while len(heap) > 0:
            number, i, j = heappop(heap)
            count += 1
            if count == k:
                return number
            if j + 1 < n:
                heappush(heap, [matrix[i][j+1], i, j+1])
                
        return number

# method - 2 
# complexity - O(n log N)
class Solution:
    
    # use staircase search method to get count
    def getCount(self, matrix, mid, n):
        
        row = 0
        col = n-1                               # start from top right corner
        count = 0
        
        while row < n and col >= 0:
            if mid >= matrix[row][col]:         # if mid is greater means that whole row has small values so add whole row as count and row ++
                count += col+1
                row += 1
            else:                               # else col -= 1
                col -= 1
        return count
        
        
    # similar to book allocation (binary search)
    def kthSmallest(self, matrix: List[List[int]], k: int):
        
        n = len(matrix)
        if n == 0:
            return 0
        
        low = matrix[0][0]                                  # 1st element is min element
        high = matrix[n-1][n-1]                             # last element is max element
        ans = 0
        while low <= high:
            mid = (low+high)//2                             # find mid
            count = self.getCount(matrix, mid, n)           # count elements less than mid
            if count >= k:                                  # if count is greater means values with lower range has ans
                ans = mid   
                high = mid-1
            else:                                           # else values with higher range has ans
                low = mid+1
        
        return ans