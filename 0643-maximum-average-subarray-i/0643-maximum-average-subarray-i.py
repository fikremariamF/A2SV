class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        average = 0
        maxAverage = 0
        for idx in range(k):
            average += nums[idx]/k
        maxAverage = average
        print(maxAverage)
        
        left, right = 0, k
        
        while right < len(nums):
            average -= nums[left]/k
            average += nums[right]/k
            maxAverage = max(average, maxAverage)
            right += 1
            left += 1
        return maxAverage
        