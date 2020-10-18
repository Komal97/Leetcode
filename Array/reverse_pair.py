'''
https://leetcode.com/problems/reverse-pairs/
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].
You need to return the number of important reverse pairs in the given array.

Example1:
Input: [1,3,2,3,1]
Output: 2

Example2:
Input: [2,4,3,5,1]
Output: 3
'''

# Use inversion count
# Calculate separately the results for ranges [start,mid] and [mid+1,end] using recursion
# Count elements in [start,mid] that are greater than 2 * elements in [mid+1,end] and add in result
class Solution:
    
    def merge(self, s, e, mid, temp, nums):
        
        count = 0
        i = s
        j = mid+1
        k = s
        
        while i <= mid and j <= e:

            if nums[i] <= nums[j]:
                temp[k] = nums[i]
                i += 1
                k += 1
            else:
                temp[k] = nums[j]
                j += 1
                k += 1
            
        
        while i <= mid:
            temp[k] = nums[i]
            i += 1
            k += 1
        
        while j <= e:
            temp[k] = nums[j]
            j += 1
            k += 1
    
        for i in range(s, e+1):
            nums[i] = temp[i]
 
    
    def mergesort(self, s, e, nums, temp):
        
        count = 0
        if s < e:
            mid = (s+e)//2

            count = self.mergesort(s, mid, nums, temp) + self.mergesort(mid+1, e, nums, temp)
            
            j = mid+1
            for i in range(s, mid+1):                               # count for each element
                while j <= e and nums[i] > 2*nums[j]:               # find all elements in second half which is smaller
                    j += 1
                count += j-(mid+1)
        
            self.merge(s, e, mid, temp, nums)
            #nums[s: e + 1] = sorted(nums[s: e + 1])

        return count
    
    def reversePairs(self, nums: List[int]) -> int:
        
        n = len(nums)
        temp = [0]*n
        
        count = self.mergesort(0, n-1, nums, temp)
        
        return count
        
        
        
        