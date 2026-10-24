class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        r = len(self.timemap[key]) - 1
        ans = ""
        while l <= r:
            mid = (l + r) // 2
            if self.timemap[key][mid][0] <= timestamp:
                ans = self.timemap[key][mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return ans
