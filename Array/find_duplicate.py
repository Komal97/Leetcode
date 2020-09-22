'''
https://leetcode.com/problems/find-the-duplicate-number/
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one duplicate number in nums, return this duplicate number.
Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [1,1]
Output: 1

Explanation - https://medium.com/@vipsb93/detect-cycle-and-find-the-duplicate-number-in-array-34a63ce0ff6b
'''

# use linked list cycle detection logic
# slow = nums[slow] and fast = nums[nums[fast]]
class Solution:
    def findDuplicate(self, nums: List[int]):
       
        slow = fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow