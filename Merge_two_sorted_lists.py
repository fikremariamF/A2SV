# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mylist = []
        node1 = list1
        node2 = list2
        if node1 == None and node2 == None:
            return None
        elif node1 == None:
            return node2
        elif node2 == None:
            return node1
            
            
        while node1 or node2:
            if node1 and node2:
                if node1.val >= node2.val:
                    mylist.append(node2.val)
                    node2 = node2.next
                else:
                    mylist.append(node1.val)
                    node1 = node1.next
            elif node1:
                while node1:
                    mylist.append(node1.val)
                    node1 = node1.next
            else:
                while node2:
                    mylist.append(node2.val)
                    node2 = node2.next
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
