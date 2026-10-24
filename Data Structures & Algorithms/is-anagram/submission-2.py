class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = defaultdict(int)
        tMap = defaultdict(int)

        for char in s:
            sMap[char] += 1
        for char in t:
            tMap[char] += 1
        
        return sMap == tMap
        