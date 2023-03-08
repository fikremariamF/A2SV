# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        output = []
        prevLevel= [root]
        while True:
            newLevel = []
            prevValues = []
            for treeNode in prevLevel:
                if treeNode.left:
                    newLevel.append(treeNode.left)
                if treeNode.right:
                    newLevel.append(treeNode.right)
                prevValues.append(treeNode.val)
            output.append(prevValues)
            if len(newLevel) == 0:
                break
            prevLevel = newLevel[:]
            
        return output
        