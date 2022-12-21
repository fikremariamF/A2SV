class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        triangle = nums[0] + nums[1] + nums[2]
        max_perimeter = 0
        if nums[0] + nums[1] > nums[2]:
            max_perimeter = triangle
        i ,j = 0, 2
        # print(max_perimeter)
        while j < len(nums)-1:
            triangle += nums[j+ 1]
            triangle -= nums[i]
            # print(i, triangle)
            i += 1
            # print(max_perimeter)
            if  nums[i] + nums[i + 1] > nums[j+1]:
                max_perimeter = max(max_perimeter, triangle)
            j += 1
        return max_perimeter
        