class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        ans = ""
        if a != 0: heapq.heappush(heap, (-a, 'a'))
        if b != 0: heapq.heappush(heap, (-b, 'b'))
        if c != 0: heapq.heappush(heap, (-c, 'c'))

        unavailable = None
        while heap:
            freq, char = heapq.heappop(heap)
            ans += char
            if len(ans) >= 2 and ans[-2:] == char + char:
                unavailable = (freq+1, char) if freq+1 != 0 else None
            else:
                if unavailable:
                    heapq.heappush(heap, unavailable)
                    unavailable = None
                if freq+1 != 0: heapq.heappush(heap, (freq+1, char))
        return ans


