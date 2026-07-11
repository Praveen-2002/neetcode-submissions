# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def rec(root):
            if not root:
                return -float('inf')
            return max(root.val + rec(root.left), root.val + rec(root.right), root.val)

        res = root.val
        queue = [root]
        while queue:
            node = queue.pop()
            if node.left != None and node.right != None:
                left, right = rec(node.left), rec(node.right)
                res = max(res, node.val+left, node.val+right, node.val+left+right)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
            res = max(res, node.val, rec(node))
        return res

        