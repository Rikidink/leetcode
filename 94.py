'''
94. Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/
'''


# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []

        def helper(node):
            if node.left:
                helper(node.left)
            res.append(node.val)
            if node.right:
                helper(node.right)
        
        helper(root)

        return res
    

x = Solution()
y = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))), TreeNode(3, None, TreeNode(8, TreeNode(9))))
print(x.inorderTraversal(y))