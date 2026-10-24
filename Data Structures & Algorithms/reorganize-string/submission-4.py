class Solution:
    def reorganizeString(self, s: str) -> str:
        frequencies = defaultdict(int)
        for char in s:
            frequencies[char] += 1
        if max(frequencies.values()) > (len(s) + 1) // 2:
            return ""

        idx = 0
        res = [''] * len(s)
        for char, freq in frequencies.items():
            while freq != 0:
                res[idx] = char
                freq -= 1
                idx += 2
                if idx >= len(s):
                    idx = 1
        return "".join(res)


        

        