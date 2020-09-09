'''
https://leetcode.com/problems/power-of-four/
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
Follow up: Could you solve it without loops/recursion?
Example 1:
Input: 16
Output: true

Example 2:
Input: 5
Output: false
'''


import math
class Solution:
    
    # method - 1 
    # 1 bit should be set => n&(n-1)==0
    # even places should not set => n & (0xAAAAAAAA) == 0
    def isPowerOfFour(self, n: int):
        return n!=0 and (n&(n-1)==0) and (n & (0xAAAAAAAA) == 0)
    
    # method - 2 => log(num)/log(4) should be whole number (floor and ceil should be equal)
    def isPowerOfFour(self, n: int):
    
        if n <= 0:
            return False
        num = math.log(n)/math.log(4)
        return math.floor(num) == math.ceil(num)