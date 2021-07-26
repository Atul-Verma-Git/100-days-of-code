class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 0
        while i < len(intervals)-1:
            if intervals[i][1] < intervals[i+1][0]:
                i += 1
            else:
                if intervals[i][1] < intervals[i+1][1]:
                    intervals[i][1] = intervals[i+1][1]
                    intervals.pop(i+1)
                else:
                    intervals.pop(i+1)
        return intervals
        