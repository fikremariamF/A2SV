class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
#         # bills.sort()
        
#         billsDict = defaultdict(int)
#         for bill in bills:
#             print(billsDict)
#             if bill == 5:
#                 billsDict[5] += 1
#             elif bill == 10:
#                 if billsDict[5] <= 0:
#                     return False
#                 billsDict[5] -= 1
#                 billsDict[10] += 1
#             else:
#                 if billsDict[10] >= 1 and billsDict[5] >= 1:
#                     billsDict[20] += 1
#                     billsDict[10] -= 1
#                     billsDict[5] -= 1
#                 elif billsDict[5] >= 3:
#                     billsDict[20] += 1
#                     billsDict[5] -= 3
#                 else:
#                     return False
#         return False
        count5, count10 = 0, 0
        for i in range(len(bills)):
            if bills[i] == 5:
                count5 += 1
            elif bills[i] == 10:
                count10 += 1
                if not count5:
                    return False
                count5 -= 1
            else:
                if count10 and count5:
                    count10 -= 1
                    count5 -= 1
                elif count5 > 2:
                    count5 -= 3
                else:
                    return False
        return True