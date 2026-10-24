class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        stones = [-el for el in stones]
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if first == second:
                continue
            else:
                heapq.heappush(stones, -abs(first-second))
        return -stones[0] if stones else 0