class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        output = []
        outputSet = set()
        tracker = []
        def findNoneDecreasing(start):
            if len(tracker) >= 2 and tuple(tracker) not in outputSet:
                output.append(tracker[:])
                outputSet.add(tuple(tracker[:]))
            if start == len(nums):
                return
            
            for idx in range(start, length):
                if not tracker:
                    tracker.append(nums[idx])
                    findNoneDecreasing(idx + 1)
                    if tracker:
                        tracker.pop()
                else:
                    if tracker[-1] <= nums[idx]:
                        tracker.append(nums[idx])
                        findNoneDecreasing(idx + 1)
                        if tracker:
                            tracker.pop()
                            
        findNoneDecreasing(0)
        
        return output
                