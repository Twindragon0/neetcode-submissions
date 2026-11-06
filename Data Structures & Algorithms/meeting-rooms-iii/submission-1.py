class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        numMeetings = [0] * n
        meetings.sort(key=lambda x: x[0])
        heap = []
        for i in range(n):
            heapq.heappush(heap, (0, i))
        for meeting in meetings:
            start, end = meeting[0], meeting[1]
            while heap[0][0] < start:
                _, roomNo = heapq.heappop(heap)
                heapq.heappush(heap, (start, roomNo))
            roomEnd, roomNo = heapq.heappop(heap)
            newStart = max(roomEnd, start)
            heapq.heappush(heap, (newStart + end - start, roomNo))
            numMeetings[roomNo] += 1
            
        maxAns = 0
        maxVal = numMeetings[0]
        for i in range(1, len(numMeetings)):
            if numMeetings[i] > maxVal:
                maxVal = numMeetings[i]
                maxAns = i
        return maxAns