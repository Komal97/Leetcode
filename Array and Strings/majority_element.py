'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2
'''

class Solution:
# method - 1 using hashmap -> o(n) time & o(n) space
    def majorityElement(self, nums: List[int]) -> int:
        h = {}
        n = int(len(nums)/2)
        
        for num in nums:
            if num not in h:
                h[num] = 1
            else:
                h[num] += 1
            
            if h[num] > n:
                return num
				
# method - 2 moore's voting algorithm -> o(n) time & o(1) space			
	def majorityElement(self, nums: List[int]) -> int:
	
        major = 0
        count = 1
        n = len(nums)
        for i in range(1, n):
            if nums[major] == nums[i]:
                count += 1
            else:
                count -= 1
            if count == 0:
                count = 1
                major = i
        
        count = 0 
        for num in nums:
            if num == nums[major]:
                count += 1
        if count > int(n/2):
            return nums[major]
        
