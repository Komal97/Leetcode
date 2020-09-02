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
    
    def findAllPaths(self, root, summ, path, allPath):
        if root == None:
            return
        
        path.append(root.val)
        
        if root.left == None and root.right == None and summ == root.val: # add path in allpaths at leaf node only
            temp = path.copy()
            allPath.append(temp)
            
        self.findAllPaths(root.left, summ-root.val, path, allPath)
        self.findAllPaths(root.right, summ-root.val, path, allPath)
        path.pop()
        
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
        path = []
        allPath = []
        self.findAllPaths(root, sum, path, allPath)
        
        return allPath