# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head and head.next:
            dummy = ListNode()
            dummy.next = head
            curr = dummy.next
            counter = 0
            while curr:
                curr = curr.next
                counter += 1
            k = k % counter 
            for _ in range(k):
                curr = dummy.next
                while curr and curr.next and curr.next.next:
                    curr = curr.next
                temp = dummy.next
                dummy.next = curr.next
                curr.next = None
                dummy.next.next = temp
            return dummy.next
        else:
            return head
        