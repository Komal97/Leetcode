'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.

Example 1:
Input:
s: "cbaebabacd" p: "abc"
Output:
[0, 6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
'''

class Solution:

# method - 1 (using 2 hashmaps) 
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        n = len(s)
        m = len(p)
        res = []
        
        hp = Counter(p)
        
        for i in range(n-m+1):
            hs = Counter(s[i:i+m])
            if hp == hs:
                res.append(i)
        return res