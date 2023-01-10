class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        forward_prefix = []
        backward_prefix = []
        
#         counts all operations from left to right
        oneCount = 0
        current = 0
        for idx in range(len(boxes)):
            forward_prefix.append(current)
            if boxes[idx] == "1":
                oneCount += 1
            current += oneCount
#         counts all the operations from right to left
        oneCount = 0
        current = 0
        for idx in range(len(boxes)-1, -1, -1):
            backward_prefix.append(current)
            if boxes[idx] == "1":
                oneCount += 1
            current += oneCount
        backward_prefix.reverse()
        
#        adds the operations both on the right and the left 
        for idx in range(len(boxes)):
            forward_prefix[idx] += backward_prefix[idx]
        return forward_prefix