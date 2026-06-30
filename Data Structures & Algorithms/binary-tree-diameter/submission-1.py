# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def depestnode(root):
            if not root:
                return 0
            return 1+ max(depestnode(root.left), depestnode(root.right))
        
        def rec(root):
            left, right = 0,0
            if not root:
                return 0
            left += depestnode(root.left)
            right += depestnode(root.right)
            return max(left+ right, rec(root.left), rec(root.right))

        return rec(root)
