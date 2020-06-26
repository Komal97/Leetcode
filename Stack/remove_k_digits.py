'''
https://leetcode.com/problems/remove-k-digits/
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.
Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"

Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
'''

# if current element is less than prv, then remove prv element
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = []
        
        for digit in num:
            
            while k > 0 and len(stack) > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        if k > 0:
            stack = stack[:-k]
            
        return "".join(stack).lstrip("0") or "0"
            