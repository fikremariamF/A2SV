class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)):
            max_height = i
            for j in range(i + 1, len(heights)):
                if heights[max_height] < heights[j]:
                    max_height = j
            names[i], names[max_height] = names[max_height], names[i]
            heights[i] , heights[max_height] = heights[max_height], heights[i]
            
        # names.reverse()
        return names
            