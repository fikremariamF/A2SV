class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        position = []
        
        if not nums:
            return [-1,-1]
        
        left, right = 0, len(nums) -1

        while left <= right:
            
            mid = (left + right) // 2
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right= mid - 1
        if -1 < left < len(nums) and nums[left] == target:        
            position.append(left)
        else:
            position.append(-1)
        
        left, right = 0, len(nums) -1
        
        while left <= right:
            
            mid = (left + right) // 2
            # print(nums[mid])
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if -1 < right < len(nums) and nums[right] == target:
            position.append(right)
        else:
            position.append(-1)
        
        return position
        
            
        