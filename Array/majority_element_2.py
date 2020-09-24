'''
https://leetcode.com/problems/majority-element-ii/
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
Note: The algorithm should run in linear time and in O(1) space.

Example 1:
Input: [3,2,3]
Output: [3]

Example 2:
Input: [1,2,2,3,2,1,1,3]
Output: [1, 2]
'''

class Solution:
    
    def findCandidate(self, nums, n):
        
        n1 = -1
        n2 = -1
        c1 = 0
        c2 = 0
        for i in range(n):
            num = nums[i]           
            # check if num is matched, then increment its counter    
            if num == n1:                   
                c1 += 1
            elif num == n2:                 
                c2 += 1
            # if not initialized then initialized, 
            # initilization is done after checking otherwise same element will be assigned to other variable as well
            elif c1 == 0:                   
                n1 = num
                c1 = 1
            elif c2 == 0:
                n2 = num
                c2 = 1
            # if not matched with anyone then decrement its count
            else:
                c1 -= 1
                c2 -= 1
                
        return n1, n2
    
    def findMajority(self, nums, n1, n2, n):
        
        c1 = 0
        c2 = 0
        for i in range(n):
            if nums[i] == n1:
                c1 += 1
            elif nums[i] == n2:
                c2 += 1
        ans = []
        if c1 > (n//3):
            ans.append(n1)
        if c2 > (n//3):
            ans.append(n2)
        return ans
    
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
     
        n1, n2 = self.findCandidate(nums, n)
        return self.findMajority(nums, n1, n2, n)
        
    