class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        roomToMeetings = defaultdict(int)
        available = [(i, 0) for i in range(n)] # min heap tracking the list of available rooms (roomNo)
        inMeeting = [] # min heap tracking the rooms in meeting (endTime, roomNo)
        meetings.sort()
        for meeting in meetings:
            while inMeeting and inMeeting[0][0] <= meeting[0]:
                endTime, roomNo = heapq.heappop(inMeeting)
                heapq.heappush(available, (roomNo, endTime))
            if not available:
                x = inMeeting[0][0]
                while inMeeting and inMeeting[0][0] <= x:
                    endTime, roomNo = heapq.heappop(inMeeting)
                    heapq.heappush(available, (roomNo, endTime))
            roomNo, startTime = heapq.heappop(available)
            heapq.heappush(inMeeting, (max(startTime, meeting[0]) + meeting[1] - meeting[0], roomNo))
            roomToMeetings[roomNo] += 1
        maxRoom, maxNo = -1, 0
        for i in range(n):
            if roomToMeetings[i] > maxNo:
                maxNo = roomToMeetings[i]
                maxRoom = i
        return maxRoom

        