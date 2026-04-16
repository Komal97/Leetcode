'''
https://leetcode.com/problems/diagonal-traverse/
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.
Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output:  [1,2,4,7,5,3,6,8,9]
'''

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if not matrix:
            return []
        
        n, m, ans = len(matrix), len(matrix[0]), []
        
        # each cell denotes the sum, every diagonal has same sum
        for i in range(n + m -1):
            if i & 1:
                for j in range(i, -1, -1):
                    # since i denotes the sum, i-j denotes the row index
                    # since j is starting from i, means value can be bigger than number of columns
                    if j < m and (i-j) < n:
                        ans.append(matrix[i-j][j])
            else:
                for j in range(i, -1, -1):
                    # it is following the same pattern but in reverse order
                    # hence j starts from i and goes to 0
                    if j < n and (i-j) < m:
                        ans.append(matrix[j][i-j])
        
        return ans
