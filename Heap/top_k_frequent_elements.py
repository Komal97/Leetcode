'''
https://leetcode.com/problems/top-k-frequent-elements/
Given a non-empty array of integers, return the k most frequent elements.
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
'''
from heapq import heapify, heappush, heapreplace

# insert in map - find frequency
# using minheap (insert pair of freq and el), find elements with top k frequency 
# complexity - O(n + nlogk)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if len(nums) <= 1:
            return nums
        ans = []
        h = {}
        
        for num in nums:
            if num not in h:
                h[num] = 1
            else:
                h[num] += 1
        
        heap = []
        
        for el in h:
            if len(heap) < k:
                heappush(heap, (h[el], el))
            elif heap[0][0] < h[el]:
                heapreplace(heap, (h[el], el))
        
        while len(heap) > 0:
            ans.append(heap[0][1])
            heappop(heap)
            
        return ans