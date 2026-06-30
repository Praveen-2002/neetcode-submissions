# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def rec(root, curr_max):
            if not root:
                return 0
            if root.val >= curr_max:
                return 1 + rec(root.left,root.val) + rec(root.right,root.val)
            return rec(root.left,curr_max) + rec(root.right,curr_max)
        return rec(root,root.val)
