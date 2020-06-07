'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution:

#method 1
    def findIndex(self, target: int, nums: List[int]):
        end = len(nums) - 1
        while(end>-1):
            if nums[end] == target:
                return end
            end -= 1
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = nums.copy()
        start = 0
        end = len(nums) - 1
        nums.sort()
        
        while start<=end:
            if nums[start] + nums[end] == target:
                i = temp.index(nums[start])
                j = self.findIndex(nums[end], temp)
                return [i, j]
            elif nums[start] + nums[end] < target:
                start+=1
            elif nums[start] + nums[end] > target:
                end-=1
            
			
#method 2 - use hash table with value as key and index as value 

		h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]