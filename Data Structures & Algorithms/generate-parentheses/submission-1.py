class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        def recurse(currN, numOpen, currStr):
            if len(currStr) == 2 * n:
                self.ans.append(currStr)
            else:
                if numOpen != 0:
                    recurse(currN, numOpen-1, currStr + ")")
                if currN != 0:
                    recurse(currN-1, numOpen+1, currStr + "(")
        recurse(n, 0, "")
        return self.ans
            