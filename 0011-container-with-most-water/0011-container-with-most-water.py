class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = -1
        i = 0
        j = len(height) - 1
        while i < j:
            if height[i] < height[j]:
                area = max(area, (j-i)*height[i])
                i += 1
            else:
                area = max(area, (j-i)*height[j])
                j -= 1
        
        return area