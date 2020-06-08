'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
1) You must do this in-place without making a copy of the array.
2) Minimize the total number of operations.
'''

class Solution:
#method 1
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = []
        size = len(nums)
        
        for i in range(size):
            if nums[i]>0:
                arr.append(nums[i])
                
        while len(arr)<size:
            arr.append(0)
        
        for i in range(len(arr)):
            nums[i] = arr[i]
			
#method 2
	def moveZeroes(self, nums: List[int]) -> None:
      
        j = 0
        size = len(nums)
        for i in range(size):
            if nums[i]!=0:
                nums[i], nums[j] = nums[j], nums[i]
                j+=1
        
        