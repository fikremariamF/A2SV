class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i, j = 1, 0
        while k > 0:
            if j >= len(arr) or arr[j] > i:
                k -= 1
            else:
                j += 1
            i += 1
        return i - 1