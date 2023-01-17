class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        maximum = max(heights)
        
        answers = [[] for _ in range(maximum)]
        # print(len(answers))
        for idx in range(len(heights)):
            # print(idx)
            # print(heights[idx])
            answers[heights[idx] - 1].append(names[idx])
        names = []
        for ans in answers:
            if ans:
                for name in ans:
                    names.append(name)
        names.reverse()
        return names
            