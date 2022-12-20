class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = len(nums1) - len(nums2)- 1
        p2 = len(nums2) - 1
        p3 = len(nums1) - 1
        while True:
            if p1 >= 0 and p2 >= 0:
                if nums1[p1] > nums2[p2]:
                    nums1[p3] = nums1[p1]
                    p3 -= 1
                    p1 -= 1
                elif nums1[p1] <= nums2[p2]:
                    nums1[p3] = nums2[p2]
                    p2 -= 1
                    p3 -= 1
            elif p2 < 0:
                break
            else:
                nums1[p3] = nums2[p2]
                p3 -= 1
                p2 -= 1
                
            