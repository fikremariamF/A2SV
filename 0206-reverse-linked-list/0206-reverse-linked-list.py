# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        tempHead = ListNode()
        curr = head
        tempHead.next = curr
        head = head.next
        curr.next = None
        while head:
            curr = head
            head = head.next
            curr.next = None
            tempCurr = tempHead.next
            tempHead.next = curr
            tempHead.next.next = tempCurr
            
        return tempHead.next