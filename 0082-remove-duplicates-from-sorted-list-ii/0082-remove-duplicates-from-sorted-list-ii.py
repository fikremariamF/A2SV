# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ptr = ListNode()
        while head:
            similar = False
            while head and head.next:
                if head.val == head.next.val:
                    similar = True
                    head = head.next
                    continue
                break
            if not similar:
                ptr.next = head
                ptr = ptr.next
            head = head.next
        ptr.next = None
        return dummy.next