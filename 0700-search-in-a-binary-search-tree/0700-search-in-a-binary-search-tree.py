# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            if stack[-1].val == val:
                return stack.pop()
            else:
                curr = stack.pop()
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
        