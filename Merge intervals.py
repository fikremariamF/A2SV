class Solution:
    def sortby(self, interval):
        return interval[0]
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = self.sortby)
        # print(intervals)
        length = len(intervals)-1
        i = 0
        while i < len(intervals)-1:
            if i == -1:
                i = 0
            if i < len(intervals)-1 and intervals[i][1] >= intervals[i+1][0]:
                if intervals[i][1] <= intervals[i+1][1]:
                    intervals[i][1] = intervals[i+1][1]
                intervals.pop(i+1)
                length -= 1
                i -= 1
            i += 1
            
        return intervals
        
