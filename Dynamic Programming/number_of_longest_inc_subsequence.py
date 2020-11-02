'''
https://leetcode.com/problems/number-of-longest-increasing-subsequence/
Given an integer array nums, return the number of longest increasing subsequences.

Example 1:
Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:
Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
'''

from collections import defaultdict
class Solution:
    def findNumberOfLIS(self, nums: List[int]):
        
        n = len(nums)
        
        # store lis
        lis = [1]*n
        
        # store ways to form current lis
        ways = [1]*n
        
        maxlen = 1
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    
                    # if lis is greater for current means no.of ways to reach j = no.of ways to reach current
                    if lis[i] < (1+lis[j]):
                        lis[i] = 1 + lis[j]
                        ways[i] = ways[j]
                    
                    # if current lis is again formed, means multiple ways so add all
                    elif lis[i] == (1+lis[j]):
                        ways[i] += ways[j]
            maxlen = max(maxlen, lis[i])
        
        # count all lis ways ( eg: at multiple points, lis of 5 can be formed)
        count = 0
        for i in range(n):
            if lis[i] == maxlen:
                count += ways[i]
        
        return count
        