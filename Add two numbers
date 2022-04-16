# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = []
        num2 = []
        remainder = 0
        while l1:
            num1.append(l1.val)
            l1 = l1.next
        while l2:
            num2.append(l2.val)
            l2 = l2.next
        num1.reverse()
        num2.reverse()
        str1 = "" 
        for x in num1:
            str1 += str(x)
        str2 = ""
        for x in num2:
            str2 += str(x)
        newnum = int(str1) + int(str2)
        num3 = []
        for i in str(newnum)[::-1]:
            num3.append(ListNode(int(i)))
        for i in range(len(num3) - 1):
            num3[i].next = num3[i+1]
        return num3[0]
        
            
