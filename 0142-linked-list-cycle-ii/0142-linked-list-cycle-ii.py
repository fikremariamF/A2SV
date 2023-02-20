# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = set()
        cycle = True
        ptr = head
        
        while ptr:
            if ptr in nodes:
                break
            nodes.add(ptr)
            ptr = ptr.next
        if cycle:
            return ptr
        return None
            