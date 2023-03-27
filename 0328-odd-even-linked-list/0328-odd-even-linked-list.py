# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = 0
        oddList = ptr1 = ListNode()
        evenList = ptr2 = ListNode()
        while head:
            if counter % 2 == 0:
                ptr1.next = head
                ptr1 = ptr1.next
            else:
                ptr2.next = head
                ptr2 = ptr2.next
            head = head.next
            counter += 1
        ptr2.next = None
        ptr1.next = evenList.next
        return oddList.next
            
            
                