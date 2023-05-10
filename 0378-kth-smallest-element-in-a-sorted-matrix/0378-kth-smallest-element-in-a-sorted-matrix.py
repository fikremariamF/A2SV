class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        newMatrix = []
        for mat in matrix:
            heapify(mat)
            newMatrix.append(mat)
        # print(newMatrix)
        matrix = newMatrix[:]
        heapify(matrix)
        sortedList = []
        
        while len(matrix) > 0:
            # print(matrix, sortedList)
            temp = heappop(matrix)
            sortedList.append(heappop(temp))
            if len(temp) > 0:
                heappush(matrix, temp)
        # print("sorted List",sortedList)
        return sortedList[k-1]
            
            
        