# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, val):
            if not root:
                return 10000;
            if root.val == val:
                return 0
            elif root.val < val:
                return 1+ helper(root.right, val)
            else:
                return 1+ helper(root.left, val)
        
        def rec(main, root, ind):
            if not root:
                return True;
            if ind != helper(main,root.val):
                return False
            return True and rec(main, root.left, ind+1) and rec(main, root.right, ind+1)

        return rec(root,root, 0)
