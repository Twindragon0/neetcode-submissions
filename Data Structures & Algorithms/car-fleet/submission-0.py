class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # positions = [4, 1, 0, 7]
        # steps = [3, 5, 10, 3] <- ceil((target - position)/speed)
        # sorted_steps = [(0, 10), (1, 5), (4, 3), (7, 3)]
        # what is the condition for a fleet? if position[i] < position[j] and steps[i] <= steps[j]
        steps = []
        for i in range(len(position)):
            pos = position[i]
            steps.append((pos, (target - pos) / speed[i]))
        steps = sorted(steps)
        stk = []
        for step in steps:
            while stk and stk[-1][1] <= step[1]:
                stk.pop()
            stk.append(step)
        return len(stk)

        