# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calcDepth(self, node)->int:
        if node:
            if node.left and node.right:
                return max(1 + self.calcDepth(node.left), 1 + self.calcDepth(node.right))
            elif node.left:
                return (1 + self.calcDepth(node.left))
            elif node.right:
                return (1 + self.calcDepth(node.right))
        return 1
            
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            return self.calcDepth(root)
        else:
            return 0