# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        track = [root]
        i = 0
        while i<len(track):
            if track[i] == None:
                i+=1
                continue
            track.append(track[i].left)
            track.append(track[i].right)
            i+=1
        res = ''
        for i in track:
            if i!=None:
                res+=str(i.val)+','
            else:
                res+='None,'
        return res[:-1]
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == '':return None
        data = data.split(',')
        node_data = []
        for i in data:
            if i=='None':
                node_data.append(None)
            else:
                node_data.append(TreeNode(int(i)))
        
        i,j = 0,0
        while i < len(node_data) and j < len(node_data)-2:
            if node_data[i] == None:
                i+=1
                continue
            node_data[i].left = node_data[j+1]
            node_data[i].right = node_data[j+2]
            i+=1
            j+=2
        return node_data[0]