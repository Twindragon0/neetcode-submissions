class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while True:
                if not stk or temperatures[stk[-1]] >= t:
                    stk.append(i)
                    break
                else:
                    res[stk[-1]] = i - stk[-1]
                    stk.pop()
        return res
