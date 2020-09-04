'''
https://leetcode.com/problems/repeated-substring-pattern/
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
Example 1:
Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Example 2:
Input: "aba"
Output: False

Example 3:
Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
'''

# find longest prefix suffix (l = lps[n-1]) using kmp preprocessing table
# if n%(n-l) = 0 means true else false
class Solution:
    def repeatedSubstringPattern(self, s: str):
        
        n = len(s)
        lps = [0]*n
        i = 0
        j = 1

        while j < n:
            if s[i] == s[j]:
                lps[j] = i+1
                i += 1
                j += 1
            else:
                if i != 0:
                    i = lps[i-1]
                else:
                    lps[j] = 0
                    j += 1
        l = lps[n-1]
        if l>0 and n%(n-l)==0:
            return True
        return False
    