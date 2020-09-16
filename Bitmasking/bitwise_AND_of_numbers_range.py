'''
https://leetcode.com/problems/bitwise-and-of-numbers-range/
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:
Input: [5,7]
Output: 4

Example 2:
Input: [0,1]
Output: 0
'''

class Solution:
    def count_bits(self, n):
        count = -1
        while(n>0):
            count += 1
            n = n>>1
        return count
    
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        
        if m == 0 or n==0:
            return 0
        if m==n:
            return m
        
        ans = 0
        while(n>0 and m>0):
            if self.count_bits(m) != self.count_bits(n):
                break
            val  = 1<< self.count_bits(m)
            ans = ans + val
            n = n - val
            m = m - val
           
        return ans