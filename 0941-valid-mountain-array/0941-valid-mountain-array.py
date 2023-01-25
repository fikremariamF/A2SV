class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        decreasing  = False
        increasing = False
        idx = 0
        while idx < len(arr) - 1:
            if arr[idx] < arr[idx + 1]:
                increasing = True
            elif arr[idx] >= arr[idx + 1]:
                break
            idx += 1
        while idx < len(arr) - 1:
            if arr[idx] > arr[idx + 1]:
                decreasing  = True
            if arr[idx] <= arr[idx + 1]:
                break
            idx += 1
        if increasing and decreasing and idx == len(arr) - 1:
            return True
        return False