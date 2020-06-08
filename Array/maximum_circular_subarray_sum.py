'''
Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.
Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)
Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)

Example 1:

Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3
'''
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        
        max_val = A[0]
        min_val = A[0]
        total = 0
        cur_max = 0
        cur_min = 0
        
        for val in A:
            cur_max = max(cur_max + val, val)
            cur_min = min(cur_min + val, val)
            max_val = max(max_val, cur_max)
            min_val = min(min_val, cur_min)
            total += val
        
        return max(total-min_val, max_val) if max_val >= 0 else max_val
            