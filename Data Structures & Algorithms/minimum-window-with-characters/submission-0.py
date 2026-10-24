class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def valid(sMap, tMap):
            for key in tMap.keys():
                if sMap[key] < tMap[key]:
                    return False
            return True

        tMap = defaultdict(int)
        for char in t:
            tMap[char] += 1
        
        l = 0
        r = 0
        sMap = defaultdict(int)
        ans = ""
        while r < len(s):
            # Increment r to the right till its a valid window
            while not valid(sMap, tMap):
                if r == len(s):
                    return ans
                if s[r] in tMap:
                    sMap[s[r]] += 1
                r += 1
            print(r)
            # Increment l to the left till its a valid window
            while valid(sMap, tMap):
                if s[l] in tMap:
                    sMap[s[l]] -= 1
                l += 1
            # Update ans
            if ans == "" or len(ans) > (r-l+1):
                ans = s[l-1:r]
        return ans

