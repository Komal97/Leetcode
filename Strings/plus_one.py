'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        n = len(digits)
        i = n-1
        while i>=0:
            value = digits[i] + 1
            if value <= 9:
                digits[i] = value
                return digits
            else:
                digits[i] = 0
                i -= 1
                
        if digits[0] == 0:
            digits[0] = 1
            digits.append(0)
            
        return digits