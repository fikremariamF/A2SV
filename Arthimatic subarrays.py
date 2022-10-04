class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def checkArth(arr):
            dif = arr[1] - arr[0]
            counter = 1
            while counter < len(arr) - 1:
                if arr[counter + 1] - arr[counter] == dif:
                    counter += 1
                    continue
                else:
                    return False
            return True
        index = 0
        output = []
        while index < len(l):
            newlist = nums[l[index]:r[index] + 1]
            newlist.sort()
            output.append(checkArth(newlist))
            index += 1
        return output
