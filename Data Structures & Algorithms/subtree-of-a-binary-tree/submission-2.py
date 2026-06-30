# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(root,subroot):
            if(not root and not subroot):
                return True
            if (root and not subroot) or (subroot and not root) or (root.val != subroot.val):
                return False
            return True and helper(root.left,subroot.left) and helper(root.right, subroot.right)
        
        def parser(root):
            if not root:
                return False
            if root.val == subRoot.val and helper(root, subRoot):
                print("Called")
                return True
            return parser(root.left) or parser(root.right)
        return parser(root)


