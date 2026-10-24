class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.ans = []
        wordDict = set(wordDict)
        def recurse(curr, myStr):
            if curr == "":
                self.ans.append(myStr.strip())
            else:
                for i in range(len(curr)):
                    if curr[:i+1] in wordDict:
                        recurse(curr[i+1:], myStr + curr[:i+1] + " ")
        recurse(s, "")
        return self.ans