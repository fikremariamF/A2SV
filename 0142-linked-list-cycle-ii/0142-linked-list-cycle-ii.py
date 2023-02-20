# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        first = True
        while (fast and slow and slow != fast) or first:
            first = False
            if fast and fast.next and fast.next.next:
                fast = fast.next.next
                if slow and slow.next:
                    slow = slow.next
                else:
                    return None
            else:
                return None
        # print(head)
        # print(fast)
        # print(slow)
        slow = head
        if fast and slow:
            while fast != slow:
                first = False
                fast = fast.next
                slow = slow.next
            return fast
        else:
            return None
            