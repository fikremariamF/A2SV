# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        rights = []
        nodes = deque()
        if root:
            nodes.append(root)
            while rights or nodes:
                # print(nodes)
                if nodes:
                    current = nodes.popleft()
                    output.append(current.val)
                    if current.left:
                        nodes.append(current.left)
                    if current.right:
                        rights.append(current.right)
                else:
                    nodes.append(rights.pop(-1))
        return output