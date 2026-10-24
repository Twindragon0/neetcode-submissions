class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def valid(sMap, tMap):
            for tKey in tMap.keys():
                if sMap[tKey] < tMap[tKey]:
                    return False
            return True
        
        ans = ""
        tMap = defaultdict(int)
        for char in t:
            tMap[char] += 1
        
        l = 0
        r = 0
        sMap = defaultdict(int)
        while r < len(s):
            sMap[s[r]] += 1
            while valid(sMap, tMap):
                ans = s[l:r+1] if ans == "" or len(ans) > len(s[l:r+1]) else ans
                sMap[s[l]] -= 1
                l += 1
            r += 1
        return ans

