# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # ptr1 = head
        # ptr2 = head
        # while ptr2 and ptr2.next:
        #     ptr1 = ptr1.next
        #     ptr2 = ptr2.next
        #     if ptr2.next:
        #         ptr2 = ptr2.next
        # return ptr1
        ptr = head
        linkedlist = []
        while ptr:
            linkedlist.append(ptr)
            ptr = ptr.next
        return linkedlist[len(linkedlist)//2]
            
                
        
        