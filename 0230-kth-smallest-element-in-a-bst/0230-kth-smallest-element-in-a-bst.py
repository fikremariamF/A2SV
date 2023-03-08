# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findItems(self, root):
        if root:
            if not root.left and not root.right:
                return [root.val]
            else:
                return self.findItems(root.left) + [root.val] +self.findItems(root.right)
        return []
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        items = self.findItems(root)
        # print(items)
        return items[k-1]