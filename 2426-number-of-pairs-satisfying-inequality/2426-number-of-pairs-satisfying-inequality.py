class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        for idx in range(len(nums1)):
            nums1[idx] -= nums2[idx]
        # print(nums1)
        count = 0
        def divide(left, right):
            if left + 1 < right:
                mid = (left + right)//2
                leftSide = divide(left,mid)
                rightSide = divide(mid, right)
                # print("suii?",leftSide, rightSide)
                merged = merge(leftSide, rightSide)
                return merged
            else:
                return [nums1[left]]
        
        def merge(left, right):
            nonlocal count
            ptr1, ptr2 = 0, 0
            output = []
            # print("to be merged",left, right)
            # print("int count",count)
            for num in right:
                # print("num", num)
                while ptr2 < len(left):
                    if left[ptr2] <= num + diff or ptr2 == len(left):
                        # print("ptr2", left[ptr2],num)
                        ptr2 += 1
                        continue
                    break
                count += ptr2
            # print("fin count",count)
            ptr1, ptr2 = 0, 0
            while ptr1 < len(left) and ptr2 < len(right):
                if left[ptr1] <= right[ptr2]:
                    output.append(left[ptr1])
                    ptr1 += 1
                else:
                    output.append(right[ptr2])
                    ptr2 += 1
            output.extend(left[ptr1:])
            output.extend(right[ptr2:])
            return output
            
        newN = divide(0, len(nums1))
        # print(newN)
        return count
            
            
            