# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def depestnode(root):
            if not root:
                return 0
            left = depestnode(root.left)
            right = depestnode(root.right)
            res[0] = max(res[0], left+right, max(left,right))
            return 1+max(left,right)
        depestnode(root)
        return res[0]
