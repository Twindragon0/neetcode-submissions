class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        self.arr.sort()
        if len(self.arr) % 2 == 0:
            return (self.arr[len(self.arr) // 2 - 1] + self.arr[len(self.arr) // 2]) / 2
        return self.arr[len(self.arr) // 2]
        