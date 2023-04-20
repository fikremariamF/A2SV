# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def iterate(node):
            if not node:
                return 
            # print(node.val)
            string = "" + str(node.val)
            if node.left:
                string += "("
                if node.left:
                    string += iterate(node.left)
                string += ")"
            if node.right:
                if not node.left:
                    string += "("
                    string += ")"
                string += "("
                string += iterate(node.right)
                string += ")"
            return string
        
        return iterate(root)