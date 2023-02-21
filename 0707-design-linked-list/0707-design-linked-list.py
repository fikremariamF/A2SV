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
            # print("===",curr.val, "=======")
        for _ in range(index):
            if curr:
                # print(curr.val)
                curr = curr.next
        if curr:
            # print("got",curr.val)
            return curr.val
        else:
            # print("got nothing")
            return -1

    def addAtHead(self, val: int) -> None:
        temp = self.dummy.next
        newNode = Node(val)
        newNode.next = temp
        self.dummy.next = newNode
        # curr = self.dummy.next
        # while curr:
        #     print(curr.val)
        #     curr = curr.next
        # print("at head added", val)

    def addAtTail(self, val: int) -> None:
        curr = self.dummy
        while curr and curr.next:
            curr = curr.next
        curr.next = Node(val)
        # curr = self.dummy.next
        # while curr:
        #     print(curr.val)
        #     curr = curr.next
        # print("added at taile", val)

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.dummy.next
        # print("about to add at index:", index, "-val:", val)
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
        curr = self.dummy.next
        # while curr:
        #     print(curr.val)
        #     curr = curr.next
        # print("==============")
    def deleteAtIndex(self, index: int) -> None:
        curr = self.dummy.next
        for _ in range(index - 1):
            if curr:
                curr = curr.next
        # print("==to be deleted==")
        # if curr:
        #     print(curr.val, index)
        # print("==to be deleted end==")
        if index == 0:
            print("Last ONE")
            if curr and curr.next:
                # print("deletting the zeroz")
                self.dummy.next = curr.next
                curr = self.dummy.next
                # while curr:
                #     print(curr.val)
                #     curr = curr.next
                # print("deleted", index)
                return
            elif curr:
                self.dummy.next = None
            else:
                return -1
        if curr and curr.next:
            temp = None
            if curr.next.next:
                temp = curr.next.next
            curr.next = temp
            curr = self.dummy.next
            # while curr:
            #     print(curr.val)
            #     curr = curr.next
            # print("deleted", index)
            return 1
        else:
            curr = self.dummy.next
            # while curr:
            #     print(curr.val)
            #     curr = curr.next
            # print("+++++++++")
            return -1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)