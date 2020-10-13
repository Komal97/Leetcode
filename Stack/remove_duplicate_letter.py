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

class Solution:
    def removeDuplicateLetters(self, s: str):
        
        n = len(s)
        if n == 0 or n == 1:
            return s
        
        # to keep track of prv processed elements
        stack = []                             
        # to keep character count, so that we can predict that current greater character is available in future or not
        cnt = Counter(s)  
        # to keep track of unique character visit               
        visited = defaultdict(bool)
        
        for ch in s:
            if visited[ch] == False:
                # check if prev pushed element is greater
                if len (stack) > 0 and stack[-1] > ch:  
                    # pop and mark not visited if stack top is greater and is available in future to consume                    
                    while len (stack) > 0 and stack[-1] > ch and cnt[stack[-1]] > 0:
                        c = stack.pop()
                        visited[c] = False
                # finally push character in stack and mark visited
                stack.append(ch)
                visited[ch] = True
            # always reduce character count to keep character count
            cnt[ch] -= 1
            
        
        return ''.join(stack)