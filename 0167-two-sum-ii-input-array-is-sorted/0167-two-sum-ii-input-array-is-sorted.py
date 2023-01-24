class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indexes = {}
        for idx in range(len(numbers)):
            indexes[numbers[idx]] = idx
        # print(indexes)
        for idx in range(len(numbers)):
            if target - numbers[idx] in indexes:
                return[idx + 1, indexes[target - numbers[idx]] + 1]
            
        