class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for idx in range(len(names)):
            heights[idx] = [names[idx],heights[idx]]
        length = len(heights) - 1
        for idx in range(len(heights)):
            i, j  = 0, 1
            for _ in range(length):
                if heights[i][1] < heights[j][1]:
                    heights[i], heights[j] = heights[j], heights[i]
                i += 1
                j += 1
            length -= 1
        for idx in range(len(heights)):
            heights[idx] = heights[idx][0]
        return heights
            