class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort(key=lambda x: x[0])
        l, r = 0, 1
        while l < len(intervals) and r < len(intervals):
            if intervals[r][0] < intervals[l][1]:
                if intervals[l][1] >= intervals[r][1]:
                    l = r
                    r += 1
                else:
                    r += 1
                ans += 1
            else:
                l = r
                r += 1
        return ans

            