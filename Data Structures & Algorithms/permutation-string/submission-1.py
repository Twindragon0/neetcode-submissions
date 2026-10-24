class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = [0] * 26
        for char in s1:
            s1Map[ord(char) - ord('a')] += 1
        
        s2Map = [0] * 26
        for i in range(len(s1)-1):
            s2Map[ord(s2[i]) - ord('a')] += 1
        
        for i in range(0, len(s2)-len(s1)+1):
            s2Map[ord(s2[i+len(s1)-1]) - ord('a')] += 1
            if s1Map == s2Map:
                return True
            s2Map[ord(s2[i]) - ord('a')] -= 1
        return False

