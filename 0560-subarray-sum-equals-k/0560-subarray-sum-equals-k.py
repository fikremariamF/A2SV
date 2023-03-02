class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = 0
        prefix_sum_dict = {0:1}
        prefix_sum = 0
        for idx in range(len(nums)):
            temp = prefix_sum + nums[idx]
            prefix_sum += nums[idx]
            if temp - k in prefix_sum_dict:
                counter += prefix_sum_dict[temp-k]
            prefix_sum_dict[temp]  = prefix_sum_dict.get(temp,0) + 1
        # print(prefix_sum_dict)
        return counter