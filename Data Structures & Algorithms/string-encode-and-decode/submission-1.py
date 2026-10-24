class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for myStr in strs:
            ans += str(len(myStr)) + "." + myStr
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        while s != "":
            idx = s.find(".")
            myLen = int(s[:idx])
            ans.append(s[idx+1:idx+1+myLen])
            s = s[idx+1+myLen:]
        return ans
        
            

