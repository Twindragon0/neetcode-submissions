class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        personToNumTrust = defaultdict(int)
        trustingN = [0] * n
        for el in trust:
            personToNumTrust[el[0]] += 1
            trustingN[el[1] - 1] += 1
        for i in range(n):
            if trustingN[i] == n-1:
                return i+1 if personToNumTrust[i+1] == 0 else -1
        return -1