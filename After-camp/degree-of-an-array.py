class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = defaultdict(int)
        first_occurrence = {}
        last_occurrence = {}
        for idx in range(len(nums)):
            count[nums[idx]] += 1
            if nums[idx] not in first_occurrence:
                first_occurrence[nums[idx]] = idx
            last_occurrence[nums[idx]] = idx
        
        degree = max(count.values())
        min_length = float('inf')
        for num, freq in count.items():
            if freq == degree:
                min_length = min(min_length, last_occurrence[num] - first_occurrence[num] + 1)

        return min_length

        
        