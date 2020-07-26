'''
https://leetcode.com/problems/k-closest-points-to-origin/submissions/
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
(Here, the distance between two points on a plane is the Euclidean distance.)
You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)
Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
'''

# method - 1
# store dist of each point in array and sort, then traverse array, find dist and store points having dist <= temp[K-1]
class Solution:
    def findDist(self, point):
        return point[0] * point[0] + point[1] * point[1]
        
        
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        temp = []
        for i in range(len(points)):
            temp.append(self.findDist(points[i]))
            
        temp.sort()
        dist = temp[K-1]
        res = []
        for i in range(len(points)):
            if self.findDist(points[i]) <= dist:
                res.append(points[i])
                
        return res

# method - 2
# use max heap to find k points with smallest dist, store (dist, (x, y))
from heapq import heappush, heapreplace, heappop
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        heap = []
        
        for i in range(len(points)):
            dist = (points[i][0]*points[i][0]) + (points[i][1]*points[i][1])
            if len(heap) < K:
                heappush(heap, (-dist, points[i]))
            elif heap[0][0] < -dist:
                heapreplace(heap, (-dist, points[i]))
                
        ans = []
        while len(heap) > 0:
            ans.append(heap[0][1])
            heappop(heap)
        
        return ans