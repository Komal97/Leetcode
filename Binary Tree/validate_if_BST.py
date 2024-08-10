'''
https://leetcode.com/problems/validate-binary-search-tree/description/
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    class Pair:
        def __init__(self):
            self.min = float('inf')
            self.max = float('-inf')
            self.isBST = True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node):
            if not node:
                p = self.Pair()
                return p
            
            lp = validate(node.left)
            rp = validate(node.right)

            pair = self.Pair()
            pair.min = min(lp.min, rp.min, node.val)
            pair.max = max(lp.max, rp.max, node.val)
            pair.isBST = lp.isBST and rp.isBST and (node.val > lp.max) and (node.val < rp.min)
            return pair

        return validate(root).isBST
