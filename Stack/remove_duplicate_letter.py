'''
https://leetcode.com/problems/remove-duplicate-letters/
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:
Input: s = "bcabc"
Output: "abc"

Example 2:
Input: s = "cbacdcbc"
Output: "acdb"
'''

from collections import Counter, defaultdict
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        # to keep track of prv processed elements
        stack = [] 
        # to keep character count, so that we can predict that current greater character is available in future or not
        cnt = Counter(s) 
         # to keep track of unique character visit          
        visited = defaultdict(bool)  
        for ch in s:
            # always reduce character count to keep character count for future characters
            cnt[ch] -= 1
            # say, if b is coming at pos 0 and pos 9, then pos 0 will be considered as that can guarantee smaller lexicographical string and can be identified with visisted
            if visited[ch] == True: 
                continue
            
            # check if prev pushed element is greater
            # pop and mark not visited if stack top is greater and is available in future to consume           
            while len(stack)>0 and ch < stack[-1] and cnt[stack[-1]] > 0:
                prev = stack.pop()
                visited[prev] = False
            # finally push character in stack and mark visited
            stack.append(ch)
            visited[ch] = True
        
        return ''.join(stack)    