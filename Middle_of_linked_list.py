# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mylist = []
        counter  = 0
        node = head
        while node:
            node = node.next
            counter += 1
        node = head
        if counter <= 1:
            return head
        
        newcounter = 1
        while newcounter <= counter:
            if newcounter > counter/2:
                return(node)
            if node.next:
                node = node.next
            newcounter += 1
        
        
