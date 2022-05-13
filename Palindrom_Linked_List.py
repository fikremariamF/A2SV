# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mylist = []
        node = head
        while node:
            mylist.append(node.val)
            node = node.next
        i = 0
        j = len(mylist)-1
        print(mylist)
        while i < j:
            if mylist[i] == mylist[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
