'''
https://leetcode.com/problems/simplify-path/
Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.
In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the directory up a level.
Note that the returned canonical path must always begin with a slash /, and there must be only a single slash / between two directory names. The last directory name (if it exists) must not end with a trailing /. Also, the canonical path must be the shortest string representing the absolute path.

Example 1:
Input: "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Example 2:
Input: "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

Example 3:
Input: "/a/../../b/../c//.//"
Output: "/c"

Example 4:
Input: "/..hidden"
Output: "/..hidden"
'''

# method - 1
class Solution:
    def simplifyPath(self, path: str):
        
        stack = []
        n = len(path)
        
        i = 0
        
        while i < n:
            if path[i] == '/':
                if len(stack) > 0 and stack[-1] == '/':
                    i += 1
                    continue
                stack.append('/')   
                i += 1
            else:
                ch = ''
                while i < n and path[i] != '/':
                    ch += path[i]
                    i += 1
                if ch == '.':
                    continue
                elif ch == '..':
                    stack.pop()
                    while len(stack) > 0 and stack[-1] != '/':
                        stack.pop()
                else:
                    stack.append(ch)

        if len(stack) > 1:
            if stack[-1] == '/':
                stack.pop()
        elif len(stack) == 0:
            stack.append('/')
        return ''.join(stack)
                        
# method - 2
# split by / and check conditions of '.' and '..'
class Solution:
    def simplifyPath(self, path: str):
        
        stack = []
        path = path.split('/')

        for ch in path:
            if ch == '.' or ch == '':
                continue
            elif ch == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(ch)
        return '/' + '/'.join(stack)