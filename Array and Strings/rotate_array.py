'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]

Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
'''

class Solution:
#method 1 --- increase size of array
    def rotate(self, nums: List[int], k: int) -> None:

        for i in range(k):
            nums.append(0)
        
        size = len(nums)-1
        
        for i in range(size, k-1, -1):
            nums[i] = nums[i-k]
        
        for i in range(k-1, -1, -1):
            nums[i] = nums[size]
            size-=1
        size +=1
        nums[:] = nums[:size]

#method 2 - reverse array and again reverse small part
	def reverse(self, nums, start, end):
        while(start<end):
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -=1
            
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)