class Solution:
    def reorganizeString(self, s: str) -> str:
        charToFreq = defaultdict(int)
        for char in s:
            charToFreq[char] += 1
        heap = []
        for char, freq in charToFreq.items():
            heapq.heappush(heap, (-freq, char))
        ans = ""
        unavailable = ""
        while heap:
            freq, char = heapq.heappop(heap)
            ans += char
            if unavailable:
                heapq.heappush(heap, unavailable)
            if freq+1 != 0:
                unavailable = (freq+1, char)
            else:
                unavailable = None
        return "" if unavailable else ans
        