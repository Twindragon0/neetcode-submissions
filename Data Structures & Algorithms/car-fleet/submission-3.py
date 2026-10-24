class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # positions = [4, 1, 0, 7]
        # speed = [2, 2, 1, 1]
        times = []
        for i in range(len(position)):
            times.append((position[i], (target - position[i]) / speed[i]))
        times = sorted(times, reverse=True)
        
        currTime = times[0][1]
        fleets = 1
        for i in range(1, len(times)):
            if times[i][1] > currTime:
                fleets += 1
                currTime = times[i][1]
        return fleets
        

        