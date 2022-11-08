class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        mylist = []
        while True:
            if mylist and mylist[-1] == popped[0]:
                mylist.pop(-1)
                popped.pop(0)
            else:
                if len(pushed) == 0:
                    break
                mylist.append(pushed[0])
                pushed.pop(0)
        
        if mylist:
            return False
        return True
