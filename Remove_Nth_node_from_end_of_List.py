# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        mylist = []
        counter  = 0
        node = head
        while node:
            node = node.next
            counter += 1
        node = head
        if counter == 1 and n == 1:
            # head.val = None
            return None
        newcount = counter - n
        while newcount > 0:
            mylist.append(node.val)
            node = node.next
            newcount -= 1
        node = node.next
        while node:
            mylist.append(node.val)
            node = node.next
        A = ListNode(mylist[0])
        if len(mylist) == 1:
            return A
        A.next = ListNode(mylist[1])
        mylist.pop(0)
        mylist.pop(0)
        B = A.next
        while len(mylist) > 0:
            B.next = ListNode(mylist[0])
            B = B.next
            mylist.pop(0)
        return A
                
            
        
            
