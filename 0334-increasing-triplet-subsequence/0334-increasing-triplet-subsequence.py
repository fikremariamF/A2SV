class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        mins = []
        
        minn = float("inf")
        for idx in range(len(nums)):
            minn = min(minn, nums[idx])
            mins.append(minn)
        
        maxx = float("-inf")
        for idx in range(len(nums) - 1, -1, -1):
            maxx = max(maxx, nums[idx])
            if mins[idx] < nums[idx] < maxx:
                return True
        return False
        
        