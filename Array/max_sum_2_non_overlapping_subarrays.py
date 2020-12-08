'''
https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/
Given an array A of non-negative integers, return the maximum sum of elements in two non-overlapping (contiguous) subarrays, which have lengths L and M.  (For clarification, the L-length subarray could occur before or after the M-length subarray.)
Formally, return the largest V for which V = (A[i] + A[i+1] + ... + A[i+L-1]) + (A[j] + A[j+1] + ... + A[j+M-1]) and either:
0 <= i < i + L - 1 < j < j + M - 1 < A.length, or
0 <= j < j + M - 1 < i < i + L - 1 < A.length.
 
Example 1:
Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
Output: 20
Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.

Example 2:
Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
Output: 29
Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.

Example 3:
Input: A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
Output: 31
Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with length 3.
'''

class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int):
        
        n = len(A)

        # precompute sum array
        for i in range(1, n):
            A[i] += A[i-1]
        
        # eg = L = 3, M = 2
        
        # option1 : take current window M = 2 and maintain prev max window L=3 value and hence maxsum
        lmax = A[L-1]
        res1 = A[L+M-1]
        for i in range(L+M, n):
            cursum = A[i] - A[i-M]
            lmax = max(lmax, A[i-M] - A[i-M-L])
            res1 = max(res1, cursum + lmax)
        
        # option2 : take current window L = 3 and maintain prev max window M = 2 value and hence maxsum
        mmax = A[M-1]
        res2 = A[L+M-1]
        for i in range(L+M, n):
            cursum = A[i] - A[i-L]
            mmax = max(mmax, A[i-L] - A[i-L-M])
            res2 = max(res2, cursum + mmax)
        
        # return max of 2 options
        return max(res1, res2)