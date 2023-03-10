# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        output = []
        path = []
        def travers(node):
            if node and not node.right and not node.left:
                temp = []
                for idx in range(len(path)):
                    temp.append(str(path[idx]))
                    temp.append("->")
                temp.append(str(node.val))
                output.append("".join(temp))
                return
            
            path.append(node.val)
            if node.left:
                travers(node.left)
            if node.right:
                travers(node.right)
            path.pop()
        
        travers(root)
        return output
                
            