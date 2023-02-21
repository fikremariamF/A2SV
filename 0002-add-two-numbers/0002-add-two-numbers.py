# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        ptr1 = l1
        ptr2 = l2
        remainder = 0
        while ptr1 and ptr2:
            currSum = ptr1.val + ptr2.val
            if remainder != 0:
                currSum += 1
                remainder = 0
            if currSum > 9:
                remainder += 1
            if currSum > 9:
                curr.next = ListNode(currSum - 10)
            else:
                curr.next = ListNode(currSum)
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            curr = curr.next
        while ptr1:
            currSum = ptr1.val
            if remainder:
                currSum += remainder
                remainder -= 1
            if currSum > 9:
                remainder += 1
                curr.next = ListNode(currSum - 10)
            else:
                curr.next = ListNode(currSum)
            ptr1 = ptr1.next
            curr = curr.next
        while ptr2:
            currSum = ptr2.val
            if remainder:
                currSum += remainder
                remainder -= 1
            if currSum > 9:
                remainder += 1
                curr.next = ListNode(currSum - 10)
            else:
                curr.next = ListNode(currSum)
            ptr2 = ptr2.next
            curr = curr.next
        if remainder > 0:
            curr.next = ListNode(remainder)
        return dummy.next
                