class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stk = []
        for i, t in enumerate(temperatures):
            while True:
                if not stk or temperatures[stk[-1]] >= t:
                    stk.append(i)
                    break
                else:
                    ans[stk[-1]] = i - stk[-1]
                    stk.pop()
        return ans 
