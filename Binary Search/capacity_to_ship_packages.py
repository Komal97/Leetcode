'''
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
A conveyor belt has packages that must be shipped from one port to another within D days.
The i-th package on the conveyor belt has a weight of weights[i].  Each day, we load the ship with packages on the conveyor belt (in the order given by weights). 
We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within D days.

Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
Output: 15
Explanation: 
A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10
'''

# same as that of book allocation problem
class Solution:
    
    def isValid(self, weights, D, max_weight):
        
        day = 1
        total_weight = 0
        for w in weights:
            total_weight += w
            if total_weight > max_weight:
                total_weight = w
                day += 1
            if day > D:
                return False
        return True
        
    def shipWithinDays(self, weights: List[int], D: int) -> int:
       
        s = 0
        e = 0
        
        s = max(weights)
        e = s * len(weights)
        
        while s<=e:
            mid = (s+e)//2
            if self.isValid(weights, D, mid):
                e = mid-1
            else:
                s = mid+1
        return s