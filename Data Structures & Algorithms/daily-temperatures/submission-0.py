class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        ans = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while True:
                if not stk:
                    stk.append(i)
                    break
                elif temp <= temperatures[stk[-1]]:
                    stk.append(i)
                    break
                else:
                    ans[stk[-1]] = i - stk[-1]
                    stk.pop()
        return ans 
