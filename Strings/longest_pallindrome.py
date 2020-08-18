'''
https://leetcode.com/problems/longest-palindrome/
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
This is case sensitive, for example "Aa" is not considered a palindrome here.
Input:
"abccccdd"
Output:
7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''

# create frequency map
# if freq is even, add it in count
# if freq is odd, add freq-1 in count because out of 3, 2 can form pallindrome
# now ans is even. if ans == string length, return ans else ans+1
class Solution:
    def longestPalindrome(self, s: str):
        
        n = len(s)
        if n == 0 or n == 1:
            return n
        
        h = {}
        
        for ch in s:
            if ch not in h:
                h[ch] = 1
            else:
                h[ch] += 1
                
        ans = 0
        for key in h:
            if h[key]%2 == 0:                   # if freq is even, add it in count
                ans += h[key]
            else:
                ans += (h[key]-1)               # if freq is odd, add freq-1 in count
            
        return ans+1 if ans < n else ans