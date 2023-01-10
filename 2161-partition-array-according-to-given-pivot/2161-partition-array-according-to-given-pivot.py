class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        output = []
        for num in nums:
            if num < pivot:
                output.append(num)
        for num in nums:
             if num == pivot:
                    output.append(pivot)
        for num in nums:
            if pivot < num:
                output.append(num)

        return output