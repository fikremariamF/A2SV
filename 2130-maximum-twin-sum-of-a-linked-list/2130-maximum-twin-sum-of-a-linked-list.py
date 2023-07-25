# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = deque()

        fast = slow = head
        while fast and fast.next:
            stack.append(slow)

            slow = slow.next
            fast = fast.next.next
        max_sum = 0
        while slow:
            max_sum = max(max_sum, slow.val + stack.pop().val)
            slow = slow.next

        return max_sum
