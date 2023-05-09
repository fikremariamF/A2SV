# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        
        tupleList = []
        i = 0
        for linkedList in lists:
            if linkedList:
                tupleList.append((linkedList.val, i, linkedList))
            i += 1
        
        heapify(tupleList)
        
        while tupleList:
            # popped =  popped[0], popped[1]
            val, i, linkedList = heappop(tupleList)
            if linkedList.next:
                heappush(tupleList, (linkedList.next.val, i, linkedList.next))
            curr.next = linkedList
            curr = curr.next 
            curr.next = None
            
        return head.next