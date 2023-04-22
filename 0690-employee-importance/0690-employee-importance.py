"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # print(employees)
        subOrdinates = deque([id])
        importance = 0
        while subOrdinates:
            temp_id = subOrdinates.pop()
            for employee in employees:
                if employee.id == temp_id:
                    for sub_id in employee.subordinates:
                        subOrdinates.append(sub_id)    
                    importance += employee.importance
        return importance
        
        