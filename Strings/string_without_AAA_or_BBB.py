'''
https://leetcode.com/problems/string-without-aaa-or-bbb/
Given two integers A and B, return any string S such that:
S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
The substring 'aaa' does not occur in S;
The substring 'bbb' does not occur in S.

Example 1:
Input: A = 1, B = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.

Example 2:
Input: A = 4, B = 1
Output: "aabaa"
'''


class Solution:
    def strWithout3a3b(self, A: int, B: int):
        
        ans = ''
        
        a = 'a'
        b = 'b'
        
        # always keep values in A larger
        if A < B:
            A, B = B, A
            a, b = b, a
        
        # similar to slow fast, move A by twice and B by one 
        while A > 0 and B > 0 and A > B:
            ans += (2*a)
            ans += b
            
            A -= 2
            B -= 1
        
        # if A <= B then move one by one both
        while A > 0 or B > 0:
            if A > 0:
                ans += a
                A -= 1
            if B > 0:
                ans += b
                B -= 1
        return ans