#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        prev = i 
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] > arr[prev]:
            prev = left
        
        if right < n and arr[right] > arr[prev]:
            prev = right
            
        if prev != i:
            arr[prev], arr[i] = arr[i], arr[prev]
            self.heapify(arr, n, prev)
        # return
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        for idx in range(n-1, -1 , -1):
            self.heapify(arr, n, idx)
        # return
                
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.buildHeap(arr,n)
        # print("arr0", arr)
        arr[-1], arr[0] = arr[0], arr[-1]
        # print("arr1", arr)
        for idx in range(n-1, 0, -1):
            self.heapify(arr, idx, 0)
            # print("newarr", arr, idx)
            arr[idx -1], arr[0] = arr[0], arr[idx -1]
        # print("arr2", arr)
        # return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends