class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        arr = [0 for _ in range(len(nums) + 1)]
        
        for request in requests:
            arr[request[0]] += 1
            arr[request[1] + 1] -= 1
        for idx in range(1,len(arr)):
            arr[idx] += arr[idx - 1]
        arr.sort(reverse = True)
        nums.sort(reverse = True)
        
        total = 0
        for idx in range(len(nums)):
            total += arr[idx] * nums[idx]
        return total % ((10**9) + 7)