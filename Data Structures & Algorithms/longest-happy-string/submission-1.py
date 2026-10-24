class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a != 0: heapq.heappush(heap, (-a, 'a'))
        if b != 0: heapq.heappush(heap, (-b, 'b'))
        if c != 0: heapq.heappush(heap, (-c, 'c'))

        res = ""
        unavailable = None
        while heap:
            freq, char = heapq.heappop(heap)
            res += char
            if unavailable:
                heapq.heappush(heap, unavailable)
                unavailable = None
            if len(res) >= 2 and res[-2:] == char + char and freq+1 != 0:
                unavailable = (freq+1, char)
            elif freq+1 != 0:
                heapq.heappush(heap, (freq+1, char))
        return res