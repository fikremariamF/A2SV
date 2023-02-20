# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = 0
        dummy = ListNode()
        dummy.next = head
        while dummy.next:
            dummy.next = dummy.next.next
            counter += 1
        if counter == 1:
            return None
        pos = counter - n
        ptr = head
        while pos > 1:
            ptr = ptr.next
            pos -= 1
        if pos == 0:
            return ptr.next
        if ptr.next.next:
            ptr.next= ptr.next.next
        else:
            ptr.next = None
        return head
                
                