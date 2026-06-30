# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def depth(root):
            if not root:
                return 0
            return 1+ max(depth(root.left), depth(root.right))
        dep = depth(root)
        for _ in range(dep):
            res.append([])
        
        def lvlOrderList(root,lvl):
            if not root:
                return
            res[lvl].append(root.val)
            lvlOrderList(root.left,1+lvl)
            lvlOrderList(root.right,1+lvl)
        lvlOrderList(root,0)

        return [x[-1] for x in res]