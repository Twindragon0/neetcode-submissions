class Solution:
    def reorganizeString(self, s: str) -> str:
        frequency = [0] * 26
        for char in s:
            frequency[ord(char) - ord('a')] += 1
        
        maxFreq = max(frequency)
        if maxFreq > (len(s) + 1) // 2:
            return ""
        
        res = ""
        while len(res) != len(s):
            charIdx = frequency.index(max(frequency))
            if len(res) >= 1 and res[-1] == chr(ord('a') + charIdx):
                tmp = frequency[charIdx]
                frequency[charIdx] = float("-inf")
                nxtIdx = frequency.index(max(frequency))
                res += chr(ord('a') + nxtIdx)
                frequency[nxtIdx] -= 1
                frequency[charIdx] = tmp
            else:
                res += chr(ord('a') + charIdx)
                frequency[charIdx] -= 1    
        return res

        

        