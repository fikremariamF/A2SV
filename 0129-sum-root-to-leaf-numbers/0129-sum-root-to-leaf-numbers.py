# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        rootToLeafs = []
        path = []
        def iterate(node):
            path.append(node.val)
            if not node.left and not node.right:
                nums = list(map(str, path))
                rootToLeafs.append(int("".join(nums)))
                path.pop()
                return
            
            if node.left:
                iterate(node.left)
            if node.right:
                iterate(node.right)
            
            path.pop()
            return
        iterate(root)
        # print(rootToLeafs)
        return sum(rootToLeafs)
            