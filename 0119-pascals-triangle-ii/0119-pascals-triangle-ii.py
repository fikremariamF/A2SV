class Solution:
    def calcRow(self, row, idx):
        curr = [1]
        if idx:
            for i in range(len(row) - 1):
                curr.append(row[i] + row[i+1])
            curr.append(1)
        
        if idx - 1 > 0:
            curr = self.calcRow(curr, idx-1)[:]
        return curr
            
    def getRow(self, rowIndex: int) -> List[int]:
        return self.calcRow([1], rowIndex)