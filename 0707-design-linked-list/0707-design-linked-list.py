class Node:
    def __init__(self, val = 0, next = None ):
        self.val = val
        self.next = next
        
class MyLinkedList:

    def __init__(self):
        self.dummy = Node()

    def get(self, index: int) -> int:
        curr = None
        if self.dummy.next:
            curr = self.dummy.next
        for _ in range(index):
            if curr:
                curr = curr.next
        if curr:
            return curr.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        temp = self.dummy.next
        newNode = Node(val)
        newNode.next = temp
        self.dummy.next = newNode

    def addAtTail(self, val: int) -> None:
        curr = self.dummy
        while curr and curr.next:
            curr = curr.next
        curr.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.dummy.next
        if index == 0:
            self.addAtHead(val)
            return
        for _ in range(index - 1):
            if curr:
                curr = curr.next
        newNode = Node(val)
        temp = None
        if curr and curr.next:
            temp = curr.next
        elif curr:
            curr.next = newNode
        else:
            return -1
        newNode.next = temp
        curr.next = newNode
    def deleteAtIndex(self, index: int) -> None:
        curr = self.dummy.next
        for _ in range(index - 1):
            if curr:
                curr = curr.next
        if index == 0:
            print("Last ONE")
            if curr and curr.next:
                self.dummy.next = curr.next
            elif curr:
                self.dummy.next = None
            else:
                return -1
        if curr and curr.next:
            temp = None
            if curr.next.next:
                temp = curr.next.next
            curr.next = temp
            return 1
        else:
            return -1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)