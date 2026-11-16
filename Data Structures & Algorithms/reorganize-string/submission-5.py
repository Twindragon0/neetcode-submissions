class Solution:
    def reorganizeString(self, s: str) -> str:
        charToFreq = defaultdict(int)
        ans = ""
        for char in s:
            charToFreq[char] += 1
        available = [(-freq, char) for (char, freq) in charToFreq.items()]
        heapq.heapify(available)
        unavailable = None
        while available:
            freq, char = heapq.heappop(available)
            ans += char
            if unavailable:
                heapq.heappush(available, (unavailable[0], unavailable[1]))
            unavailable = (freq+1, char) if freq+1 != 0 else None
        return "" if unavailable else ans