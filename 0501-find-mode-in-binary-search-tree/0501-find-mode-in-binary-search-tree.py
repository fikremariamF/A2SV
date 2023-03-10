# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        count = dict()
        def traverse(node):
            if node:
                count[node.val] = count.get(node.val, 0) + 1
                
            if node and node.left:
                traverse(node.left)
            if node and node.right:
                traverse(node.right)
        
        traverse(root)
        maximum = count[max(count, key=lambda x:count[x])]
        
        for key in count:
            if count[key] == maximum:
                output.append(key)
        
        return output
        