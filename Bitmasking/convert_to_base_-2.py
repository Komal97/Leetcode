'''
https://leetcode.com/problems/convert-to-base-2/
Given a number N, return a string consisting of "0"s and "1"s that represents its value in base -2 (negative two).
The returned string must have no leading zeroes, unless the string is "0".

Example 1:
Input: 2
Output: "110"
Explantion: (-2) ^ 2 + (-2) ^ 1 = 2

Example 2:
Input: 3
Output: "111"
Explantion: (-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0 = 3

Example 3:
Input: 4
Output: "100"
Explantion: (-2) ^ 2 = 4
'''

# with base 2
class Solution:
    def base2(self, N: int):
        
        if N == 0:
            return '0'

        x = ''
        
        while N:
            x = str(N&1) + x
            N = (N>>1)
            
        return x
    
# with base -2

# method - 1
class Solution:
    def baseNeg2(self, N: int):
        
        
        # same as base 2
        if N == 0:
            return '0'

        x = ''
        while N:
            x = str(N&1) + x
            N = -(N>>1)             # only change here
            
        return x

# method - 2 
class Solution:
    def baseNeg2(self, N: int):
        
        negBase = -2
        
        if N == 0:
            return '0'
        
        x = ''
        while N:
            rem = N % negBase
            N //= negBase
            
            if rem < 0:
                # if rem become -ve, then make it positive
                rem = rem - negBase  # -1 -(-2) => -1 + 2 => 1
                # inc N by 1
                N += 1
                
            x = str(rem) + x
        
        return x     
        