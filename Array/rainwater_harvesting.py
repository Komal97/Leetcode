'''
https://leetcode.com/problems/trapping-rain-water/
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

# method - 1 => max(height of building on left of current building - right) - height of current building
class Solution:
    def trap(self, height: List[int]):

        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]

        left[0] = height[0]
        right[n-1] = height[n-1]
        for i in range(1, n):
            left[i] = max(left[i-1], height[i])

        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i])

        count = 0
        for i in range(n):
            count += (min(left[i], right[i]) - height[i])

        print(count)

# method - 2 => since left max array always inc and right max array always dec
# so from prv method observation -> keep leftmax and rightmax
# if leftmax < rightmax then find capacity += (leftmax-height[start]) and inc start
# and same for rightmax and dec end
class Solution:
    def trap(self, height: List[int]):
        
        
        n = len(height)
        
        if n < 1:
            return 0
        
        start = 0 
        end = n-1
        leftmax = height[start]
        rightmax = height[end]
        capacity = 0
        while start <= end:
            if rightmax < leftmax:
                rightmax = max(rightmax, height[end])
                capacity += (rightmax - height[end])
                end -= 1
            else:
                leftmax = max(leftmax, height[start])
                capacity += (leftmax - height[start])
                start += 1
            
        return capacity
                
            