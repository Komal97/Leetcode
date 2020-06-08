'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
'''
class Solution:
    
    def find_first_occ(self, nums, target):
        
        start = 0
        end = len(nums) - 1
        ans = -1
        
        while start <= end:
            mid = int((start + end)/2)
            
            if nums[mid] == target:
                ans = mid 
                end = mid - 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return ans
                
        
    def find_last_occ(self, nums, target):

        start = 0
        end = len(nums) - 1
        ans = -1
        
        while start <= end:
            mid = int((start + end)/2)
            
            if nums[mid] == target:
                ans = mid 
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return ans
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        output = [-1, -1]
        
        output[0] = self.find_first_occ(nums, target)
        output[1] = self.find_last_occ(nums, target)
        
        return output