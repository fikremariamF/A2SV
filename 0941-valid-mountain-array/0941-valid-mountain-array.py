class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        decreasing  = False
        increasing = False
        idx = 0
        while idx < len(arr) - 1:
            # print(idx)
            if arr[idx] < arr[idx + 1]:
                increasing = True
            elif arr[idx] >= arr[idx + 1]:
                break
            idx += 1
        # print("==============")
        while idx < len(arr) - 1:
            # print(idx)
            if arr[idx] > arr[idx + 1]:
                decreasing  = True
            if arr[idx] <= arr[idx + 1]:
                break
            idx += 1
        # print(increasing, decreasing)
        # if arr[-1] < arr[-2]:
        #     decreasing = True
        if increasing and decreasing and idx == len(arr) - 1:
            return True
        return False