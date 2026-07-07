# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, pre_ord: List[int], in_ord: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return
        root = TreeNode(pre_ord[0])
        d = {pre_ord[0]: root}
        prev = root

        i, j = 1, 0
        right_child = False
        if prev.val == in_ord[0]:
            right_child = True 
            j+=1
        while i<len(pre_ord):
            newNode = TreeNode(pre_ord[i])
            prev_changed = False
            d[pre_ord[i]] = newNode
            if pre_ord[i] != in_ord[j]:
                if not right_child:
                    prev.left = newNode
                else:
                    prev.right = newNode
                right_child = False
            else:
                if not right_child:
                    prev.left = newNode
                else:
                    prev.right = newNode
                right_child = True
                while j<len(in_ord) and d.get(in_ord[j]) != None:
                    prev_changed = True
                    j+=1
            if not prev_changed:
                prev = newNode
            else:
                prev = d[in_ord[j-1]]
            i+=1
        return root
                
