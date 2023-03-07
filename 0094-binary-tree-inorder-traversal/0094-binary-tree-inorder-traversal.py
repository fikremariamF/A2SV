# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node):
        arr = []
        if node:
            if node.left and node.right:
                arr += self.traverse(node.left)
                arr.append(node.val)
                arr += self.traverse(node.right)
            elif node.left:
                arr += self.traverse(node.left) 
                arr.append(node.val)
            elif node.right:
                arr.append(node.val)
                arr += self.traverse(node.right)
            else:
                arr.append(node.val)
        return arr
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.traverse(root)