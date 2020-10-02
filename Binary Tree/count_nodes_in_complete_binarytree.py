'''
https://leetcode.com/problems/count-complete-tree-nodes/
Given a complete binary tree, count the number of nodes.
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. 
It can have between 1 and 2h nodes inclusive at the last level h.
Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
'''

# recursive solution - O(N)
class Solution:
    def countNodes(self, root: TreeNode):
        
        def count(root):
            if root == None:
                return 0
            
            lc = count(root.left)
            rc = count(root.right)
            return lc+rc+1
        
        return count(root)

# itertive - O(log N)^2
# outer loop of depth - O(log N) and inner loop to check complete binary tree is also O(log N)
class Solution:
    
    # if leftmost node of left subtree is full, means left tree is complete binary tree
    def isCompleteTree(self, node, depth):
        
        ptr = node
        for i in range(depth):
            if ptr is None:
                return False
            ptr = ptr.right
        return True
            
    
    def countNodes(self, root: TreeNode):
        
        if root == None:
            return 0
        elif root.left == None:
            return 1
        elif root.right == None:
            return 2
        
        ptr, depth = root, 0
        while ptr:
            ptr = ptr.left
            depth += 1
        
        ptr = root
        count = 0

        for i in range(depth-1, 0, -1):         # last level can be empty for some nodes 
            # if left is complete binary tree, add all nodes of left tree and check right subtree
            if self.isCompleteTree(ptr.left, i):            
                count += (2**i)-1
                ptr = ptr.right
            # else in right, last level is empty so add all nodes of right subtree of level-1
            else:
                count += (2**(i-1))-1
                ptr = ptr.left

            # add one root node
            count += 1


        return count+1 if ptr else count