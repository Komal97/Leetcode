'''
https://leetcode.com/problems/check-completeness-of-a-binary-tree/
Given a binary tree, determine if it is a complete binary tree.
Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example 1:
Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
'''

from collections import deque

# use level order
# maintain flag to check left and right child, if any missing then set flag = True and while checking left and right child, if flag = true then return false
# flag signifies left or child child of prev node is missing at same level
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        
        if root == None:
            return True
        
        q = deque()
        q.append(root)
        flag = False
        
        while len(q) > 0:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if node.left:
                    if flag == True:     # if we see node before which no right node of prv parent
                        return False
                    q.append(node.left)
                else:
                    flag = True         # change flag to denote that left child is missing
                if node.right:
                    if flag == True:    # if we see node before which no left node occur of same parent
                        return False
                    q.append(node.right)
                else:
                    flag = True         # change flag to denote that right child is missing
                    
        return True