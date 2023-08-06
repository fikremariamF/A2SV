class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        start = values[0]
        max_value = float('-inf')
        
        for j in range(1, len(values)):
            max_value = max(max_value, start + values[j] - j)
            start = max(start, values[j] + j)
        
        return max_value 