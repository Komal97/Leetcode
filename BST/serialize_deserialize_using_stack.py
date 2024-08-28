'''
https://leetcode.com/problems/serialize-and-deserialize-bst/
Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.
The encoded string should be as compact as possible.

Example 1:
Input: root = [2,1,3]
Output: [2,1,3]

Example 2:
Input: root = []
Output: []
'''

# method 1 using recursion
class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def traverse(node, arr):
            if node == None:
                arr.append('null')
                return
            arr.append(str(node.val))
            traverse(node.left, arr)
            traverse(node.right, arr)
        
        arr = []
        traverse(root, arr)
        return ' '.join(arr)
            
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def construct(idx):
            
            if arr[idx[0]] == 'null':
                return None
            
            n = TreeNode(int(arr[idx[0]]))
            idx[0] += 1
            n.left = construct(idx)
            idx[0] += 1
            n.right = construct(idx)
            return n
        
        arr = data.split()
        idx = [0]
        return construct(idx)
    
# method 2 using iterative algorithm   
class Codec:

    def serialize(self, root: TreeNode):
        """
        Encodes a tree to a single string.
        """
        if root == None:
            return ''
        stack = []
        stack.append([root, 0])
        
        s = ''
        while len(stack) > 0:
            node, level = stack[-1]
            if level == 0:
                stack[-1][1] += 1
                if node.left:
                    stack.append([node.left, 0])
            elif level == 1:
                stack[-1][1] += 1
                if node.right:
                    stack.append([node.right, 0])
            else:
                s += str((stack.pop())[0].val) + ' '
             
        return s.strip()
    
    def deserialize(self, data: str):
        """
        Decodes your encoded data to tree.
        """
        s = data.split()
        n = len(s)
        
        if n == 0:
            return None
    
        stack = []
        
        root = TreeNode(int(s[n-1]))
        stack.append(root)
        
        for i in range(n-2, -1, -1):
            
            num = int(s[i])
            node = TreeNode(num)
            if num >= stack[-1].val:
                stack[-1].right = node
            else:
                temp = None
                while len(stack) > 0 and stack[-1].val > num:
                    temp = stack.pop()
                temp.left = node
                
            stack.append(node)
                
        return root
