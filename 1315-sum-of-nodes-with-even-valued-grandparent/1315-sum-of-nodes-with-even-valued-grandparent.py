# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        nodes = deque([root])
        
        output = 0
        while nodes:
            node = nodes.popleft()
            if node.val % 2 == 0:
                if node.left and node.left.left:
                    output += node.left.left.val
                if node.left and node.left.right:
                    output += node.left.right.val
                if node.right and node.right.left:
                    output += node.right.left.val
                if node.right and node.right.right:
                    output += node.right.right.val
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return output
                