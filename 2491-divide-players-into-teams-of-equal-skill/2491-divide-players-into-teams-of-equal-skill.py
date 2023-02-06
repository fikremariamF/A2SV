class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        groupSkill = skill[0] + skill[-1] 
        left, right = 0 ,len(skill) - 1
        total = 0
        while left <= right:
            if skill[left] + skill[right] == groupSkill:
                total += skill[left] * skill[right]
                left += 1
                right -= 1
            else:
                return -1
        return total