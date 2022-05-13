# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        mylist = []
        node = head
        while node:
            mylist.append(node.val)
            node = node.next 
        newval = float('-inf')
        i = 0
        j = len(mylist)-1
        while i < j:
            newval = max(mylist[i]+ mylist[j], newval)
            j -= 1
            i += 1
        return newval
