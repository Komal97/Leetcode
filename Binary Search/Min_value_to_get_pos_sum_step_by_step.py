'''
Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.
'''
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        n = len(nums)
        sum_value = 0
        minimum = 1
        
        for i in range(n):
            sum_value = sum_value + nums[i]
            minimum = min(sum_value, minimum)
            
        if minimum == 1:
            return 1
        
        return abs(minimum) + 1