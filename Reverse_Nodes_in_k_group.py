# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0:
            return head
        mylist = []
        node = head
        while node:
            mylist.append(node.val)
            node = node.next
        i = 0
        while i < len(mylist):
            j = i
            l = i + k - 1
            while l < len(mylist) and j < l:
                mylist[j],mylist[l] = mylist[l],mylist[j]
                j += 1
                l -= 1
            i += k
        if len(mylist) == 0:
            return None
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
            
