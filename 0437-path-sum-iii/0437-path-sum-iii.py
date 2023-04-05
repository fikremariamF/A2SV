# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        stack = []
        count = 0
        def traverseTree(node):
            # print("node", node.val)
            nonlocal count
            stack.append(node.val)
            # print(stack)
            total = 0
            ptr = len(stack) - 1
            while ptr > -1:
                total += (stack[ptr])
                # print("total", total, ptr)
                ptr -= 1
                if total == targetSum:
                    count += 1
                    # break
                
            # print(count)
            if node.left:
                traverseTree(node.left)
                stack.pop()
                
            if node.right:
                traverseTree(node.right)
                stack.pop()
                
            return
        
        traverseTree(root)
        
        return count