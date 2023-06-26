# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        i=[0]
        def construct(preorder,i,bound):
            if i[0]==len(preorder) or preorder[i[0]]>bound:
                return None
            root=TreeNode(preorder[i[0]])
            i[0]+=1
            root.left=construct(preorder,i,root.val)
            root.right=construct(preorder,i,bound)
            return root                           
        return construct(preorder,i,float('inf'))