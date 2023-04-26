# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levels = [[root]]
        averages = []
        for level in levels:
            nodes = []
            total = 0
            for node in level:
                total += node.val
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            if nodes:
                levels.append(nodes)
            
            averages.append(total/len(level))
            
        return averages
            