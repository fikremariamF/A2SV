class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        maximum = max(heights)
        
        answers = [[] for _ in range(maximum)]
        for idx in range(len(heights)):
            answers[heights[idx] - 1].append(names[idx])
        names = []
        for idx in range(len(answers) -1 , -1, -1):
            if answers[idx]:
                for name in answers[idx]:
                    names.append(name)
        # names.reverse()
        return names
            