class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        milestones.sort()
        t = milestones[-1]
        b = sum(milestones[:-1])
        if sum(milestones[:-1]) >= t:
            return b + t
        else:
            return 2 * b + 1
