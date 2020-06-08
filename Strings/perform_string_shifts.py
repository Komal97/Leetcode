'''
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

direction can be 0 (for left shift) or 1 (for right shift). 
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.

Example 1:
Input: s = "abc", shift = [[0,1],[1,2]]
Output: "cab"
Explanation: 
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"

Example 2:
Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
Output: "efgabcd"
Explanation:  
[1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -> "efgabcd"
'''

class Solution:
    def reverse(self, s: str, start: int, end: int):
        s = list(s)
        while(start < end):
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1  
        s = ''.join(s)     
        return s
    
    def stringShift(self, s, shift) -> str:
        
        n = len(shift)
        count = 0
        
        for i in range(n):
            if shift[i][0] == 0:
                count += shift[i][1]
            elif shift[i][0] == 1:
                count -= shift[i][1]
        
        str_n = len(s)
        count = count % str_n
        
        if count == 0:
            return s
        elif count < 0:
            # right shift
            count = abs(count)
            s = self.reverse(s, 0, str_n-1)
            s = self.reverse(s, 0, count-1)
            s = self.reverse(s, count, str_n-1)
        else:
            # left shift
            s = self.reverse(s, 0, str_n-1)
            s = self.reverse(s, 0, str_n - count-1)
            s = self.reverse(s, str_n - count, str_n-1)
        return s