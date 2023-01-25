class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxNum = arr[-1]
        arr[-1] = -1
        for idx in range(len(arr) - 2, -1, -1):
            currMax = maxNum
            maxNum = max(currMax, arr[idx])
            arr[idx] = currMax
        return arr
        