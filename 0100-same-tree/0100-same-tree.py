# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pQueue = deque()
        qQueue = deque()
        
        if p and q:
            if p.val != q.val:
                return False
        
            pQueue.append(p)
            qQueue.append(q)
        
            proceed = True
            
            while pQueue and qQueue:
                if len(pQueue) == len(qQueue) and pQueue[0].val == qQueue[0].val:
                    p = pQueue.popleft()
                    q = qQueue.popleft()
                    
                    if type(p.left) == type(q.left):
                        if p.left:
                            pQueue.append(p.left)
                        if q.left:
                            qQueue.append(q.left)
                    else:
                        return False
                    
                    if type(p.right) == type(q.right):
                        if p.right:
                            pQueue.append(p.right)
                        if q.right:
                            qQueue.append(q.right)
                    else:
                        return False
                else:
                    return False
            return True
        if type(p) == type(q):
            return True
        return False
                
            
            