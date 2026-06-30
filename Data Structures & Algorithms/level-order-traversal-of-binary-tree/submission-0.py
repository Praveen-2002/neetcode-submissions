# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def depth(root):
            if not root:
                return 0
            return 1+ max(depth(root.left), depth(root.right))
        
        res=[]
        dep = depth(root)
        for _ in range(dep):
            res.append([])

        def rec(root, lvl):
            if not root:
                return;
            res[lvl].append(root.val)
            rec(root.left, 1+lvl)
            rec(root.right, 1+lvl)
        rec(root,0)
        return res