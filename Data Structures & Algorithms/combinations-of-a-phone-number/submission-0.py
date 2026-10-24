class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digToLetter = defaultdict(list)
        digToLetter["2"] = ["a", "b", "c"]
        digToLetter["3"] = ["d", "e", "f"]
        digToLetter["4"] = ["g", "h", "i"]
        digToLetter["5"] = ["j", "k", "l"]
        digToLetter["6"] = ["m", "n", "o"]
        digToLetter["7"] = ["p", "q", "r", "s"]
        digToLetter["8"] = ["t", "u", "v"]
        digToLetter["9"] = ["w", "x", "y", "z"]

        self.ans = []
        def recurse(letters, curr):
            if curr == "":
                if letters != "":
                    self.ans.append(letters)
            else:
                for letter in digToLetter[curr[0]]:
                    recurse(letters + letter, curr[1:])
        recurse("", digits)
        return self.ans
