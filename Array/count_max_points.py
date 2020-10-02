'''
https://leetcode.com/problems/max-points-on-a-line/
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:
Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4

Example 2:
Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
'''

from collections import defaultdict
class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a%b)
    
    def maxPoints(self, points: List[List[int]]):
        
        n = len(points)
        maxpoints = 0
        
        # a line is formed when one point connect to multiple points with same slope
        for i in range(n):
            
            slope = defaultdict(int)
            overlap = vertical = curmax = 0
            
            for j in range(i+1, n):
                
                # if points overlap
                if points[i] == points[j]:
                    overlap += 1
                # if points are on same vertical line
                elif points[i][0] == points[j][0]:
                    vertical += 1
                # else find slope
                else:
                    x = points[j][0] - points[i][0]
                    y = points[j][1] - points[i][1]
                    
                    # find gcd between num and den to cancel out common in num and den
                    g = self.gcd(x, y)
                    x /= g
                    y /= g
                    
                    slope[(x, y)] += 1
                    curmax = max(curmax, slope[(x, y)])
                    
                # take max of all slopes and vertical
                curmax = max(curmax, vertical)
            
            # take max of prv max and curmax + overlapping + ith point
            maxpoints = max(maxpoints, curmax + overlap + 1)
            
        return maxpoints