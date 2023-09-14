class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        hash_map = {}
        for previous_index in range(len(nums)):
            for next_index in range(previous_index + 1 , len(nums)):
                difference = nums[next_index] - nums[previous_index]
                if (previous_index , difference) not in hash_map:
                    hash_map[(next_index , difference)] = 1 + 1
                else:
                    hash_map[(next_index , difference)] = hash_map[(previous_index , difference)] + 1 
        result = max(hash_map.values())
        return result