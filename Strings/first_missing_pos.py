'''
First Missing Positive
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
Input: [1,2,0]
Output: 3

Example 2:
Input: [3,4,-1,1]
Output: 2
 
Note:Your algorithm should run in O(n) time and uses constant extra space.
'''

#https://ide.codingblocks.com/s/203342
class Solution:

#method 1
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        j = 0
        
        for i in range(len(nums)):
            if nums[i]<0:
                nums[i],nums[j] = nums[j],nums[i]
                j+=1
        
        if len(nums) < 1:
            return 1
        maximum = max(nums)
    
        temp = [0 for i in range(maximum+2)]
        
        for i in range(len(nums)):
            if nums[i] > 0:
                temp[nums[i]] = -1
                
        for i in range(1, len(temp)):
            if temp[i] == 0:
                return i
				
#method 2
	def separate(self, nums):
        size = len(nums)
        j = 0
    
        for i in range(size):
            if nums[i]<=0:
                nums[i],nums[j] = nums[j],nums[i]
                j+=1
        return j
    
    def findMissPos(self, nums):
        size = len(nums)
        
        for j in range(size):
            if abs(nums[j])-1 < size and nums[abs(nums[j])-1] > 0:
                nums[abs(nums[j])-1] = -nums[abs(nums[j])-1]
            
     
        for k in range(size):
            if nums[k]>0:
                return k+1
        return size + 1
        
    def firstMissingPositive(self, nums: List[int]) -> int:
        shift = self.separate(nums)
        return self.findMissPos(nums[shift:])
        

				