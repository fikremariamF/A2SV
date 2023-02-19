# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        # print(ptr)
        while head:
            # print(head.val)
            if head.next:
                found = True
                curr = head.next
                while head.val == curr.val:
                    if curr.next:
                        curr = curr.next
                    else:
                        found = False
                        head.next = None
                        break
                if found:
                    head.next = curr
            head = head.next
        # print(ptr)
        return ptr