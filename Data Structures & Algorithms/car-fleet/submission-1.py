class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # positions = [4, 1, 0, 7]
        # speed = [2, 2, 1, 1]
        times = []
        for i in range(len(position)):
            times.append((position[i], (target - position[i]) / speed[i]))
        times = sorted(times)
        stk = []
        for time in times:
            while stk and stk[-1][1] <= time[1]:
                stk.pop()
            stk.append(time)
        return len(stk)
        

        