class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        for i in range(len(self.timemap[key])):
            if self.timemap[key][i][0] <= timestamp:
                ans = self.timemap[key][i][1]
        return ans
