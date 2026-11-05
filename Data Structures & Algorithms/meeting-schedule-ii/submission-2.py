"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        heap = []
        for interval in intervals:
            if not heap:
                heapq.heappush(heap, interval.end)
                continue
            if interval.start < heap[0]:
                heapq.heappush(heap, interval.end)
            else:
                oldMax = heapq.heappop(heap)
                heapq.heappush(heap, max(interval.end, oldMax))
        return len(heap)
            


