class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) -1
        while left <= right:
            # print(left, right)
            mid = (left + right) // 2
            
        # claculate the change both to the left and right of the mid value it will be +1 or -1
            gradient1 = (arr[mid] - arr[mid + 1])//abs(arr[mid] - arr[mid + 1])
            gradient2 = (arr[mid - 1] - arr[mid])//abs(arr[mid - 1] - arr[mid])
            # print(mid, gradient1, gradient2)
            #if the change to the left and right is different then it means we found the peak of the mountaint
            if gradient1 != gradient2:
                return mid
            # If the change is -1 then we are on the decreasing side of the mountaint
            elif gradient1 == 1:
                right = mid 
            else:
                left = mid + 1
        return left+ 1