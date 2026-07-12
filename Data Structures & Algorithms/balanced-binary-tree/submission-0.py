# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def depth(root):
            if not root:
                return 0
            return 1 + max(depth(root.left), depth(root.right))
        
        def rec(root):
            if not root:
                return True
            if abs(depth(root.left) - depth(root.right)) > 1:
                return False
            return True and rec(root.left) and rec(root.right)

        return rec(root)