class Solution:
    def reorganizeString(self, s: str) -> str:
        frequencies = defaultdict(int)
        for char in s:
            frequencies[char] += 1
        
        heap = []
        for char, freq in frequencies.items():
            heapq.heappush(heap, (-freq, char))
        
        unavailable = None
        res = ""
        while heap:
            freq, char = heapq.heappop(heap)
            res += char
            if unavailable:
                heapq.heappush(heap, unavailable)
                unavailable = None
            if freq+1 != 0:
                unavailable = (freq+1, char)
            else:
                unavailable = None
        return "" if unavailable else res


        

        