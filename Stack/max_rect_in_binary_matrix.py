'''
https://leetcode.com/problems/maximal-rectangle/
Given a binary matrix. Find the maximum area of a rectangle formed only of 1s in the given matrix.

Input:
The first line of input is an integer T denoting the no of test cases . Then T test cases follow. The first line of each test case are 2 integers n and m denoting the size of the matrix M . 
Then in the next line are n*m space separated values of the matrix M.
Input
1
4 4 
0 1 1 0 1 1 1 1 1 1 1 1 1 1 0 0

Output
8

Explanation
For the above test case the matrix will look like
0 1 1 0
1 1 1 1
1 1 1 1
1 1 0 0
the max size rectangle is 
1 1 1 1
1 1 1 1
and area is 4 *2 = 8
'''
# same as finding maximum histogram area, just convert 2-D matrix to 1-D matrix
# for converting to 1-D, visualize binary matrix as histogram and create 1-D array after including each row, i.e at each level
class Solution:
    def rightSmallElement(self, arr, n):
        stack = []
        right = []
        for i in range(n-1, -1, -1):
            while len(stack) > 0 and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if len(stack) == 0:
                right.append(n)
            else:
                right.append(stack[-1])
            stack.append(i)
        right = right[::-1]
        return right

    def leftSmallElement(self, arr, n):
        stack = []
        left = []
        for i in range(n):
            while len(stack) > 0 and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if len(stack) == 0:
                left.append(-1)
            else:
                left.append(stack[-1])
            stack.append(i)
        return left

    def maxHistogramArea(self, arr, n):

        left = self.leftSmallElement(arr, n)
        right = self.rightSmallElement(arr, n)

        maxArea = -1
        for i in range(n):
            width = right[i] - left[i] - 1
            area = width * arr[i]
            maxArea = max(maxArea, area)
        return maxArea
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        n = len(matrix)
        if n==0:
            return 0
        m = len(matrix[0])
        
        for i in range(m):
            matrix[0][i] = int(matrix[0][i])
        result = self.maxHistogramArea(matrix[0], m)
        
        for i in range(1, n):
            for j in range(m):
                if matrix[i][j] == '1':
                    matrix[i][j] = int(matrix[i][j]) + int(matrix[i-1][j])
                else:
                    matrix[i][j] = int(matrix[i][j])
            result = max(result, self.maxHistogramArea(matrix[i], m))
        return result