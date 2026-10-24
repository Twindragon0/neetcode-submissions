class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        ts = 0
        i = 0
        endToCapacity = defaultdict(int)
        while i < len(trips) or endToCapacity:
            if ts in endToCapacity:
                capacity += endToCapacity[ts]
                endToCapacity.pop(ts)
            if i < len(trips) and trips[i][1] == ts:
                capacity -= trips[i][0]
                endToCapacity[trips[i][2]] += trips[i][0]
                i += 1
                if capacity < 0:
                    return False
                continue
            ts += 1
        return True