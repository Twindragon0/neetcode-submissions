class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        buckets = [0] * (max(stones)+1)
        for stone in stones:
            buckets[stone] += 1
        first = max(stones)
        while first > 0:
            if buckets[first] % 2 == 0:
                first -= 1
                continue
            second = first - 1
            while buckets[second] == 0 and second > 0:
                second -= 1
            if second == 0:
                return first
            buckets[first] -= 1
            buckets[second] -= 1
            buckets[first-second] += 1
            first = max(second, first-second)
        return first
            
