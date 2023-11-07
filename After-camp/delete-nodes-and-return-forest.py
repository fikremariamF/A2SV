# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        roots = [root]
        
        to_delete_set = set(to_delete)
        remaining_forest = []

        def dfs(node, is_root):
            if not node:
                return None
            node_deleted = node.val in to_delete_set
            if is_root and not node_deleted:
                remaining_forest.append(node)
            node.left = dfs(node.left, node_deleted)
            node.right = dfs(node.right, node_deleted)
            return None if node_deleted else node

        dfs(root, True)
        return remaining_forest