class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            return self.addBinary(b, a)
        a = "0" * (len(b)-len(a)) + a

        carryOn = 0
        ans = ""
        for i in range(len(a)-1, -1, -1):
            res = int(a[i]) + int(b[i]) + carryOn
            if res >= 2:
                carryOn = 1
            else:
                carryOn = 0
            ans = str(res % 2) + ans
        return str(1) + ans if carryOn == 1 else ans