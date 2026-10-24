class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        numTrusted = [0] * n
        numTrust = [0] * n
        for el in trust:
            numTrusted[el[1] - 1] += 1
            numTrust[el[0] - 1] += 1
        
        for i in range(len(numTrusted)):
            if numTrusted[i] == n-1:
                return i+1 if numTrust[i] == 0 else -1 
        return -1
        