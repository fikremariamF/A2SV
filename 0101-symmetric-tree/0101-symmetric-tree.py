# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, left, right):
        if not left or not right:
            return (not left and not right)
        
        if left.val == right.val:
            return (self.check(left.left, right.right) and self.check(left.right, right.left))
        
        return False
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.check(root.left, root.right)