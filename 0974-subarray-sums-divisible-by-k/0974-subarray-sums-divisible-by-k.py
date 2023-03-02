class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counter = 0
        prefix_sum_dict = {0:1}
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            temp = prefix_sum % k
            if temp in prefix_sum_dict:
                counter += prefix_sum_dict[temp]
            prefix_sum_dict[temp] = prefix_sum_dict.get(temp, 0) + 1
        return counter