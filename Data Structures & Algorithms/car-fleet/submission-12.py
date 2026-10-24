class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = []
        for i in range(len(position)):
            times.append((position[i], (target - position[i]) / speed[i]))
        times = sorted(times, reverse=True)
        prevTime = times[0][1]
        fleets = 1
        for i in range(1, len(times)):
            if times[i][1] > prevTime:
                prevTime = times[i][1]
                fleets += 1
        return fleets
        

        