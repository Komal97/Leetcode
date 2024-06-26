'''
https://leetcode.com/problems/single-element-in-a-sorted-array/
You are given a sorted array consisting of only integers where every element appears exactly twice, 
except for one element which appears exactly once. Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10
'''


# recursive function
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        n = len(nums)
        s = 0
        e = n-1
        
        def find(nums, s, e):
            if s>e:
                return -1
            if s == e:
                return nums[s]
            
            mid = s + int((e-s)/2)
            
            if mid%2 == 0:
                if nums[mid] == nums[mid+1]:
                    return find(nums, mid+2, e)
                else:
                    return find(nums, s, mid)
            else:
                if nums[mid] == nums[mid-1]:
                    return find(nums, mid+1, e)
                else:
                    return find(nums, s, mid-1)
        return find(nums, s, e)
                

#iterative function]
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums)
        s = 0
        e = n-1
        res = -1

        while s <= e:
            mid = s + (e-s)//2

            if s == e:
                res = s
                break

            if mid%2 == 0:
                if mid+1 < n and nums[mid] == nums[mid+1]:
                    s = mid+2
                else:
                    e = mid
            else:
                if mid-1 >=0 and nums[mid] == nums[mid-1]:
                    s = mid + 1
                else:
                    e = mid-1
        
        return nums[res]