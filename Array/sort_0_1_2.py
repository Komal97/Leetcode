'''
https://leetcode.com/problems/sort-colors/
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Follow up:
Could you solve this problem without using the library's sort function?
Could you come up with a one-pass algorithm using only O(1) constant space?
Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [0,1,2,0,1,2]
Output: [0,0,1,1,2,2]

Example 3:
Input: nums = [0]
Output: [0]
'''

# keep 3 pointers to check -> high = 2, low = 0, mid = 1
# if mid = 0, swap with low then low += 1 & mid += 1
# if mid = 1, mid += 1
# else swap mid with high, high -= 1
# similar to sort_0_1, following partitioning method
# i = 0 region, j = 1 region, k = 2 region
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        k = len(nums)-1

        while j <= k:
            if nums[j] == 1:    # if j is in correct region
                j += 1
            elif nums[j] == 0:  # if j found 0, means move to i region
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            else:               # if j found 2, means move to k region
                nums[k], nums[j] = nums[j], nums[k]
                k -= 1
        