#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        idx = 0
        while idx <len(arr) - 1:
            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
            idx += 1
            
        
    
    def selectionSort(self, arr,n):
        #code here
        arr.sort()
        # for _ in range(len(arr)):
        #     self.select(arr, _)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends