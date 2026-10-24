class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        for i, trip in enumerate(trips):
            currCapacity = trip[0]
            for j in range(i):
                if trips[j][2] > trips[i][1]:
                    currCapacity += trips[j][0]
            if currCapacity > capacity:
                return False
        return True