class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        tracker = {0:1}
        total = 0
        count = 0
        for num in nums:
            total += num
            if total - goal in tracker:
                count += tracker[total - goal]
                # tracker[total-goal] += 1
            tracker[total] = tracker.get(total, 0) + 1
        return count