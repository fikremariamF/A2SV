# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = list1
        ptr2 = list2
        output = ListNode()
        curr = output
        while ptr2 and ptr1:
            if ptr1.val <= ptr2.val:
                curr.next = ptr1
                curr = ptr1
                ptr1 = ptr1.next
            else:
                curr.next = ptr2
                curr = ptr2
                ptr2 = ptr2.next
        if ptr1:
            curr.next = ptr1
        if ptr2:
            curr.next= ptr2
        return output.next