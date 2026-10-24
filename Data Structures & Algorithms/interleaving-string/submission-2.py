class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.memo = defaultdict(bool)
        def recurse(s1, s2, s3, s1Turn):
            if (s1, s2, s3, s1Turn) in self.memo:
                return self.memo[(s1, s2, s3, s1Turn)]
            if s1 == "" and s2 == "" and s3 == "":
                return True
            if s1Turn:
                ans = False
                for i in range(1, len(s1)+1):
                    if s3.startswith(s1[:i]):
                        ans = ans or recurse(s1[i:], s2, s3[i:], False)
                self.memo[(s1, s2, s3, s1Turn)] = ans
                return ans
            else:
                ans = False
                for i in range(1, len(s2)+1):
                    if s3.startswith(s2[:i]):
                        ans = ans or recurse(s1, s2[i:], s3[i:], True)
                self.memo[(s1, s2, s3, s1Turn)] = ans
                return ans
        return recurse(s1, s2, s3, True) or recurse(s1, s2, s3, False)
            