# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cn_position = 1
        current_node = head
        start = head
        while cn_position < left:
            start = current_node
            current_node = current_node.next
            cn_position +=1
        newlist = None
        tail = current_node
        while cn_position >= left and cn_position <= right:
            next_node = current_node.next
            current_node.next = newlist
            newlist = current_node
            current_node = next_node
            cn_position +=1
        start.next = newlist
        tail.next =current_node
        if left >1:
            return head
        else:
            return newlist