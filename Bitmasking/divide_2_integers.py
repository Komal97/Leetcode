'''
https://leetcode.com/problems/divide-two-integers/
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.
 
Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.

Example 3:
Input: dividend = 0, divisor = 1
Output: 0
'''

# take a = 10, b = 3
# step 1: 10 - (3) = 7
# step 2: 7 - (3*2) = 1
# step 3: 1 - (3*4) = ...
# each time subtract double the number which we subtracted last time and add number of time in ans 
class Solution:
    def divide(self, A: int, B: int):
        
        if B == 1:
            return A
       
        a = abs(A)
        b = abs(B)
        res = 0
        while a - b >= 0:
            x = 0
            while (a - (b << x)) >= 0:      # 3*1, 3*2, 3*4.... where b = 3 and 2*(..) = x
                a -= (b<<x)
                res += (1 << x)
                x += 1
        
        # check sign
        ans = res if ((A >=0 ) == (B >=0)) else -res
        
        # check integer overflow
        return ((2**31)-1) if ans < (-(2**31)) or ans > ((2**31) - 1) else ans