'''
https://leetcode.com/problems/subarrays-with-k-different-integers/
Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.
(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)
Return the number of good subarrays of A.

Example 1:
Input: A = [1,2,1,2,3], K = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].

Example 2:
Input: A = [1,2,1,3,4], K = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
'''

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int):
        
        # cnt = count number of distict number
        # prefix_count = numbers with same distinct number in which we shrink our window
        m = collections.defaultdict(int)
        cnt, prefix_count, res, left = 0, 0, 0, 0
        
        for right in range(len(A)):
            m[A[right]] += 1
            if m[A[right]] == 1:
                cnt += 1
            
            if cnt > K:                 # start new window with new distinct elements thats why make prefix 0
                m[A[left]] -= 1
                left += 1
                cnt -= 1
                prefix_count = 0
            
            while m[A[left]] > 1:
                m[A[left]] -= 1
                left += 1
                prefix_count += 1
            
            if cnt == K:
                res += prefix_count + 1
        
        return res
                