class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timeToPassengers = defaultdict(int)
        minStart = trips[0][1]
        maxEnd = trips[0][2]
        for trip in trips:
            num, start, end = trip[0], trip[1], trip[2]
            timeToPassengers[start] += num
            timeToPassengers[end] -= num
            minStart = min(start, minStart)
            maxEnd = max(end, maxEnd)
        curr = 0
        for time in range(minStart, maxEnd+1):
            if time in timeToPassengers:
                curr += timeToPassengers[time]
            if curr > capacity:
                return False
        return True 
         