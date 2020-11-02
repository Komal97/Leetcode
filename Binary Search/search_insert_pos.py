'''
https://leetcode.com/problems/search-insert-position/
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        start = 0
        n = len(nums) - 1
        end = n
        ans = 0
        
        while(start <= end):
            mid = int((start + end)/2)
            
            if nums[mid] < target:
                ans = mid + 1
                start = mid + 1
                
            else:
                end = mid - 1
        
        return ans