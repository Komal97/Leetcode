'''
https://leetcode.com/problems/group-anagrams/
Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:
All inputs will be in lowercase.
The order of your output does not matter.
'''

# method - 1 => since it requires sorted string as key, complexity = O(NKlog(K))
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]):
            
        group = defaultdict(list)
        
        for s in strs:    
            string = ''.join(sorted(s))
            group[string].append(s)
        
        res = []
        for s in group:
            res.append(group[s])
        
        return res

# method - 2 => anagrams have same character count, so keep a count array and make that as key,
# complexity = O(NK)
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        group = defaultdict(list)
        
        for s in strs:    
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1
            #string = ''.join(sorted(s))
            group[tuple(count)].append(s)
        
        res = []
        for s in group:
            res.append(group[s])
        
        return res