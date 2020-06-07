'''
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

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        my_dict = {}
        
        for i in range(len(strs)):
            key = ''.join(sorted(strs[i]))
            if key not in my_dict:
                my_dict[key] = []
            my_dict[key].append(strs[i])
            
        strs = []
        
        for key in my_dict:
            strs.append(my_dict[key])
            
        return strs
        