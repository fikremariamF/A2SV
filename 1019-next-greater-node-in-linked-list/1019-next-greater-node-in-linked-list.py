# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        output = []
        dummy = ListNode()
        dummy.next = head
        counter = 0
        while head:
            output.append(0)
            while stack and stack[-1][1] < head.val:
                output[stack.pop()[0]] = head.val
            stack.append([counter, head.val])
            head = head.next
            counter += 1
        return output