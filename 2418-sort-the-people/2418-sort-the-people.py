class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        idx = 1
        while idx < len(names):
            case = True
            cur = idx
            while case and cur > 0:
                # print(cur)
                if heights[cur] < heights[cur - 1]:
                    case = False
                else:
                    heights[cur], heights[cur - 1] = heights[cur - 1], heights[cur]
                    names[cur], names[cur - 1] = names[cur - 1], names[cur]
                    cur -= 1
            idx += 1
         
        return names
            