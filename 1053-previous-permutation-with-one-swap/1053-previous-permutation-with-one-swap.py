class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        ind = -1
        for i in range(len(arr)-1,0,-1):
            if arr[i-1]>arr[i]:
                ind = i-1
                break
        if ind==-1: return arr

        for i in range(len(arr)-1,ind,-1):
            if arr[i]<arr[ind] and arr[i]!=arr[i-1]:
                arr[i],arr[ind] = arr[ind],arr[i]
                break

        return arr
