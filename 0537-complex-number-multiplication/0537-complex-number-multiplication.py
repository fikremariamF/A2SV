class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        nums1 = num1.split("+")
        nums2 = num2.split("+")
        
        outputs = []
        
        outputs.append(int(nums1[0]) * int(nums2[0]))
        outputs.append(int(nums1[0]) * int(nums2[1][:-1]))
        outputs.append(int(nums1[1][:-1]) * int(nums2[0]))
        outputs.append(-(int(nums1[1][:-1]) * int(nums2[1][:-1])))
        outputs[0] = outputs[0] + outputs[-1]
        outputs[1] += outputs[2]
        outputs.pop()
        outputs.pop()
        return str(outputs[0]) + "+" + str(outputs[1]) + "i"