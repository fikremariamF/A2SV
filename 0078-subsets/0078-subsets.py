class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        subSets = []
        curr = []
        foundSet = set()
        subSet_set = set() 
        def findSubsets(arr, ptr):
            if tuple(sorted(arr)) not in subSet_set:
                subSets.append(sorted(arr[:]))
                subSet_set.add(tuple(sorted(arr)))
            
            
            for idx in range(ptr, length):
                if nums[idx] not in foundSet:
                    arr.append(nums[idx])
                    foundSet.add(nums[idx])
                    findSubsets(arr, ptr + 1)
                    arr.pop()
                    foundSet.remove(nums[idx])
                    
            return
        
        findSubsets([], 0)
        
        return subSets