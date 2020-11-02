'''
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
'''
# method - 1
# keep a stack, add first right node in stack then left node
# attach popped node right to stack top and make left = None
class Solution:
    def flatten(self, root: TreeNode):
        
        if root == None:
            return
        stack = []
        stack.append(root)
        
        while len(stack) > 0:
            node = stack.pop()
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            
            if len(stack) > 0:
                node.right = stack[-1]
            node.left = None

# method - 2
# morris traversal - O(1) space
class Solution:
    def flatten(self, root: TreeNode):
        
        head = root
        
        while head.right or head.left:
            if head.left:
                t = head.left
                while t.right:
                    t = t.right
                
                t.right = head.right
                head.right = head.left
                head.left = None
                
            head = head.right
        
        return root