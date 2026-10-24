class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        def recurse(currStr, numOpen, balance):
            if numOpen == n and balance == 0:
                self.ans.append(currStr)
            if numOpen < n:
                recurse(currStr + "(", numOpen+1, balance+1)
            if balance > 0:
                recurse(currStr + ")", numOpen, balance-1)
        recurse("", 0, 0)
        return self.ans
            