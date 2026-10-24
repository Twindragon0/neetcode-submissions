class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = defaultdict(int)
        for char in s1:
            s1Map[char] += 1
        
        for i in range(len(s2)):
            s2Map = defaultdict(int)
            for j in range(i, len(s2)):
                s2Map[s2[j]] += 1
                if s1Map == s2Map:
                    return True
        return False