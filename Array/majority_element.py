'''
https://leetcode.com/problems/majority-element/
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
    def majorityElement(self, nums: List[int]):
        h = {}
        n = int(len(nums)/2)
        
        for num in nums:
            if num not in h:
                h[num] = 1
            else:
                h[num] += 1
            
            if h[num] > n:
                return num

class Solution:
    # Moore Voting Algorithm
    # overall idea is - take 1 majority element as compare other elements, which do not match they cancel out each 
    # other's count
    def find_candidate(self, arr, n):
        
        count = 1                               # take first element as majority element(maintain index)
        maj_index = 0
        
        for i in range(1, n):
            if arr[maj_index] == arr[i]:        # if maj_index and curr same, then count ++
                count += 1
            else:
                count -= 1                      # else count--

            if count == 0:                      # if count become 0 then take current element as majority element 
                count = 1
                maj_index = i
                
        return arr[maj_index]           

    def is_majority(self, el, arr, n):
        
        count = 0
        for i in range(n):
            if arr[i] == el:
                count += 1
        
        return n//2 < count 

    def majorityElement(self, nums: List[int]):
        n = len(nums)
        candidate = self.find_candidate(nums, n)                              # find candidate using algo
        return candidate if self.is_majority(candidate, nums, n) else -1      # check candidate frequency
        