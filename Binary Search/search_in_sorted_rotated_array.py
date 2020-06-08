'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
'''

class Solution:
    
    def search_value(self, nums, target, start, end):
        
        if start > end:
            return -1
        
        mid = int((start + end)/2)
        
        if nums[mid] == target:
            return mid
        
        if nums[start] <= nums[mid]:
            if nums[start] <= target and target <= nums[mid]:
                return self.search_value(nums, target, start, mid)
            else:
                return self.search_value(nums, target, mid + 1, end)
        if nums[mid] <= target and target <= nums[end]:
            return self.search_value(nums, target, mid + 1, end)
        return self.search_value(nums, target, start, mid)
        
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        return self.search_value(nums, target, start, end)