# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def insert(self,root, node):
        
        if root:
            
            if node.val > root.val:
                if root.right:
                    self.insert(root.right, node)
                else:
                    root.right = node
                    
            elif node.val < root.val:
                if root.left:
                    self.insert(root.left, node)
                else:
                    root.left = node
                    
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        head = root
        
        newNode = TreeNode(val)
        
        if not root:
            return newNode
        
        self.insert(root, newNode)
        
        return head