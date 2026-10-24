class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.ans = []
        def isPalindrome(s):
            l, r = 0, len(s)-1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        def recurse(lst, curr):
            if curr == "":
                self.ans.append(lst.copy())
            else:
                for i in range(len(curr)):
                    if isPalindrome(curr[:i+1]):
                        lst.append(curr[:i+1])
                        recurse(lst, curr[i+1:])
                        lst.pop()
        recurse([], s)
        return self.ans
