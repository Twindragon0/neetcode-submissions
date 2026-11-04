class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort(key=lambda x: x[0])
        i = 0
        while i < len(intervals):
            currEnd = intervals[i][1]
            j = i + 1
            while j < len(intervals):
                if intervals[j][0] > currEnd:
                    break
                currEnd = max(currEnd, intervals[j][1])
                j += 1
            ans.append([intervals[i][0], currEnd])
            i = j
        return ans


        