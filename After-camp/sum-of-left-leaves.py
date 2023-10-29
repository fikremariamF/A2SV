# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def isLeaf(node):
            return node and not node.left and not node.right

        if not root:
            return 0

        sum = 0

        if isLeaf(root.left):
            sum += root.left.val

        sum += self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

        return sum