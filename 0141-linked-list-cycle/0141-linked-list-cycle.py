# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = set()
        increased = True
        prev = len(nodes)
        while head and increased:
            nodes.add(head)
            head= head.next
            if len(nodes) == prev:
                return True
            else:
                prev = len(nodes)
        if increased:
            return False
        return True