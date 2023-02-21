class ListNode:
    def __init__(self, page: str, next = None):
        self.page = page
        self.next = next
        
class BrowserHistory:
    def __init__(self, homepage: str):
        self.rootPage = ListNode(homepage)
        self.stack = [self.rootPage]

    def visit(self, url: str) -> None:
        newPage = ListNode(url)
        self.stack[-1].next = newPage
        self.stack.append(newPage)

    def back(self, steps: int) -> str:
        while len(self.stack) > 1 and steps > 0:
            self.stack.pop()
            steps -= 1
        return self.stack[-1].page

    def forward(self, steps: int) -> str:
        curr = self.stack[-1]
        while curr and curr.next and steps > 0:
            self.stack.append(curr.next)
            curr = curr.next
            steps -= 1
        print(steps)
        if steps == 0:
            return curr.page
        return self.stack[-1].page

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)