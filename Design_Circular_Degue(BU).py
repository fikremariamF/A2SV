class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = [-1] * k
        self.head = 0
        self.tail = 0

    def insertFront(self, value: int) -> bool:
        # print(type(self.queue), self.queue)
        if self.queue[self.head] == -1:
            self.queue[self.head] = value
            self.head -= 1
            if self.head < 0:
                self.head += len(self.queue)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        n = self.tail + 1
        if n == len(self.queue):
            n = n % len(self.queue)
        if self.queue[n] == -1:
            self.queue[n] = value
            self.tail = n
            return True
        return False

    def deleteFront(self) -> bool:
        n = self.head + 1
        if n == len(self.queue):
            n = n % len(self.queue)
        if self.queue[n] == -1:
            return False
        self.queue[n] = -1
        self.head = n
        return True

    def deleteLast(self) -> bool:
        n = self.tail
        if self.queue[n] == -1:
            return False
        self.queue[n] = -1
        self.tail = n - 1
        if self.tail < 0:
            self.tail = self.tail + len(self.queue)
        return True

    def getFront(self) -> int:
        n = self.head + 1
        if n == len(self.queue):
            n = n % len(self.queue)
        return self.queue[n]

    def getRear(self) -> int:
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        for val in self.queue:
            if val != -1:
                return False
        return True

    def isFull(self) -> bool:
        for val in self.queue:
            if val == -1:
                return False
        return True


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
