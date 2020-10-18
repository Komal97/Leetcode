'''
https://leetcode.com/problems/valid-triangle-number/
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

Example 2:
Input: [6,4,9,7,8]
Output: 10
'''

# triangle property = sum of 2 sides > third side (all 3 combinations)
# if sum of 2 small sides > largest side then above property holds true
# so keep 1 max side fixed(iterate reverse) and s = 0 and e = i-1 and count between s and e
class Solution:
    def triangleNumber(self, nums: List[int]):
        
        
        n = len(nums)
        if n < 3:
            return 0
        
        count = 0
        nums.sort()
        
        for i in range(n-1, 1, -1):
            l = 0
            r = i-1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    count += (r-l)
                    r -= 1
                else:
                    l += 1
        
        return count