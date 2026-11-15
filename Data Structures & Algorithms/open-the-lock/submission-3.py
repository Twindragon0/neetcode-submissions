class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        seen = set()
        seen.add("0000")
        queue = deque()
        queue.append(("0000", 0))
        if "0000" in deadends:
            return -1
        while queue:
            comb, num = queue.popleft()
            if comb == target:
                return num
            for i in range(len(comb)):
                digit = int(comb[i])
                combList = list(comb)
                combList[i] = str((digit+1) % 10)
                if "".join(combList) not in seen and "".join(combList) not in deadends:
                    seen.add("".join(combList))
                    queue.append(("".join(combList), num+1))
                combList[i] = str((digit-1) % 10)
                if "".join(combList) not in seen and "".join(combList) not in deadends:
                    seen.add("".join(combList))
                    queue.append(("".join(combList), num+1))
        return -1