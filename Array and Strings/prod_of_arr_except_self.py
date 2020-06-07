'''
Product of Array Except Self

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.
Note: Please solve it without division and in O(n).
'''

#method 1
import numpy as np
import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        np.set_printoptions(legacy='1.13')
        log_nums = np.log(nums)
        sum = 0
        output = []
        for i in range(len(log_nums)):
            sum +=log_nums[i]
            
            
        for i in range(len(log_nums)): 
            output.append(round(np.exp(sum-log_nums[i])))
        output = np.array(output, int)
        return output
		
#method 2
	def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = []
        output.append(1)
        
        for i in range(1, len(nums)):
            output.append(output[i-1]*nums[i-1])
        
        r = 1
        
        i = len(output)-1
        while i>=0:
            output[i] = output[i]*r
            r = r*nums[i]
            i-=1
        return output