class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left_index , right_index = 0, len(nums) - 1

        def bin_search(l_index,r_index) -> int:
            if l_index == r_index:
                return l_index
            mid_index =  l_index+ int((r_index-l_index)/2)            
            if nums[mid_index] < nums[mid_index+1]:
                return bin_search(mid_index+1,r_index)
            else:
                return bin_search(l_index,mid_index)

        return bin_search(left_index,right_index)
