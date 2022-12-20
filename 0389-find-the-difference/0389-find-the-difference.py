class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        Scount = Counter(s)
        Tcount = Counter(t)
        for value in Tcount:
            # print(value not in Tcount)
            if value not in Scount or Scount[value] < Tcount[value]:
                return value
        
        