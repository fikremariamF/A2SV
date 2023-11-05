class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = [int(time[:2]) * 60 + int(time[3:]) for time in timePoints]
        minutes.sort()
        
        min_diff = 24 * 60
        for i in range(len(minutes)):
            diff = (minutes[(i + 1) % len(minutes)] - minutes[i]) % (24 * 60)
            min_diff = min(min_diff, diff)
        min_diff = min(min_diff, 24 * 60 - min_diff)

        return min_diff
        