class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        return nums
#         def quickSort(start, end):
#             if end - start < 1:
#                 return
#             pivot = nums[start]
#             write = start + 1
#             for read in range(start + 1, end):
#                 if nums[read] <= pivot:
#                     nums[read], nums[write] = nums[write], nums[read]
#                     write += 1
#                 print(nums)
#             print("out", start, end)
#             nums[start], nums[write-1] = nums[write-1], nums[start]
#             quickSort(start, write-2)
#             quickSort(write, end)
            
#         quickSort(0, len(nums))
#         return nums
            