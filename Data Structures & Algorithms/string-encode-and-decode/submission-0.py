class Solution:

    def encode(self, strs: List[str]) -> str:
        myStr = ""
        for s in strs:
            myStr += str(len(s)) + "a" + s
        return myStr

    def decode(self, s: str) -> List[str]:
        ans = []
        while s != "":
            idxA = s.find('a')
            strLen = int(s[0:idxA])
            ans.append(s[idxA+1:idxA+1+strLen])
            s = s[idxA+1+strLen:]
        return ans
            

