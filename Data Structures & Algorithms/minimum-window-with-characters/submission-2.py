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
        for i in range(len(s)):
            sMap = defaultdict(int)
            for j in range(i, len(s)):
                sMap[s[j]] += 1
                if valid(sMap, tMap):
                    ans = s[i:j+1] if ans == "" or len(ans) > len(s[i:j+1]) else ans
                    break
        return ans

