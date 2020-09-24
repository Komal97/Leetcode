'''
https://leetcode.com/problems/count-of-smaller-numbers-after-self/
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
'''

# use inversion count while sorting in descending order
# increment count at actual index of number, for that keep number and index pair
class Solution:
    
    def merge(self, nums, s, e, mid, temp, ans):
        
        i = s
        j = mid+1
        k = s
        while i <= mid and j <= e:
            if nums[i][0] <= nums[j][0]:
                temp[k] = nums[j]
                k += 1
                j += 1
            else:
                temp[k] = nums[i]
                ans[nums[i][1]] += (e - j + 1)
                k += 1
                i += 1
        while i <= mid:
            temp[k] = nums[i]
            k += 1
            i += 1
        
        while j <= e:
            temp[k] = nums[j]
            k += 1
            j += 1
            
        for i in range(s, e+1):
            nums[i]= temp[i]
             
    def mergesort(self, nums, s, e, temp, ans):

        if s < e:
            mid = (s+e)//2
            self.mergesort(nums, s, mid, temp, ans)
            self.mergesort(nums, mid+1, e, temp, ans)
            self.merge(nums, s, e, mid, temp, ans)
            
        
    def countSmaller(self, nums: List[int]):
        
        n = len(nums)
        temp = [0]*n
        ans = [0]*n
        nums = [[nums[i], i] for i in range(n)]
        self.mergesort(nums, 0, n-1, temp, ans)
        return ans