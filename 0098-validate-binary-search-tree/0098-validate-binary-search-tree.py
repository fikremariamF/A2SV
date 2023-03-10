# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        isValid = True
        
        def traverse(node):
            nonlocal isValid
            # print(node.val)
            minimum, maximum = node.val, node.val
            if isValid:
            
                if node and not node.left and not node.right:
                    return node.val, node.val
                if node and node.left:
                    left, right = traverse(node.left)
                    # print("left",node.val, left, right, isValid)
                    if (left >= node.val or right >= node.val):
                        isValid = False
                    else:
                        minimum = left
                    # print("left",node.val, left, right, isValid)

                if node and node.right:
                    left, right = traverse(node.right)
                    # print("right", node.val, left, right, isValid)
                    if (right <= node.val or left <= node.val):
                        isValid = False

                    else:
                        maximum = right
                    # print("right", node.val, left, right, isValid)
                    
            return minimum, maximum
        
        traverse(root)
        
        return isValid