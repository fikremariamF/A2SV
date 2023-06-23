class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        def non_circle_rob(start:int, end:int) -> int:
            curr_rob = 0
            nei_rob = 0
            nei_nei_rob = 0
            for i in range(start, end):
                curr_rob = max(nei_rob, nei_nei_rob + nums[i])
                nei_nei_rob = nei_rob
                nei_rob = curr_rob
            return nei_rob
        return max(non_circle_rob(0,len(nums)-1), non_circle_rob(1,len(nums)))
            