'''
https://leetcode.com/problems/number-complement/
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
'''

class Solution:
    def countBits(self, num: int):
        count = -1
        while(num):
            num = num >> 1
            count += 1
        return count
        
    # method - 1
    def findComplement(self, num: int):
        
        c = self.countBits(num)
        mask = 0
        while(c>=0):
            mask = mask | (1<<c)
            c -= 1
        
        num = num ^ mask
        
        return num
    
    # method - 2
    def findComplement(self, num: int):
        
        bit_count = self.countBits(num)
        
        # num = 5 = 101
        # c = 3
        # 2^3 = 8 = 1000 
        # mask = 8-1 = 7 = 111
        # num^mask = 101^111
        
        mask = (1 << (bit_count)) - 1
        return num^mask