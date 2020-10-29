'''
https://leetcode.com/problems/path-sum-ii/
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
Note: A leaf is a node with no children.

Example:
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:
[
   [5,4,11,2],
   [5,8,4,5]
]
'''

# always append a copy of path while appending in allpaths
# otherwise if path array change, that array in allpaths will also change because we append reference
class Solution:
    
    def pathSum(self, root: TreeNode, sum: int):
        
        def findAllPath(node, summ, path):
            if node == None:
                return
            
            if node.left == None and node.right == None and node.val == summ:
                allPath.append(path + [node.val])
                return
            
            findAllPath(node.left, summ - node.val, path + [node.val])
            findAllPath(node.right, summ - node.val, path + [node.val])
        
        allPath = []
        findAllPath(root, sum, [])
        return allPath