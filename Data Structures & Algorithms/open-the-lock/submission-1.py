class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        combinations = [[[[-1 for _ in range(10)] for _ in range(10)] for _ in range(10)] for _ in range(10)]
        combinations[0][0][0][0] = 0
        queue = deque()
        queue.append((0, 0, 0, 0, 0))
        while queue:
            a, b, c, d, val = queue.popleft()
            if str(a) + str(b) + str(c) + str(d) == target:
                return val

            if combinations[(a+1) % 10][b][c][d] == -1 and str((a+1) % 10) + str(b) + str(c) + str(d) not in deadends:
                queue.append(((a+1) % 10, b, c, d, val+1))
                combinations[(a+1) % 10][b][c][d] = val+1
            if combinations[a][(b+1) % 10][c][d] == -1 and str(a) + str((b+1) % 10) + str(c) + str(d) not in deadends:
                queue.append((a, (b+1) % 10, c, d, val+1))
                combinations[a][(b+1) % 10][c][d] = val+1
            if combinations[a][b][(c+1) % 10][d] == -1 and str(a) + str(b) + str((c+1) % 10) + str(d) not in deadends:
                queue.append((a, b, (c+1)%10, d, val+1))
                combinations[a][b][(c+1) % 10][d] = val+1
            if combinations[a][b][c][(d+1) % 10] == -1 and str(a) + str(b) + str(c) + str((d+1) % 10) not in deadends:
                queue.append((a, b, c, (d+1) % 10, val+1))
                combinations[a][b][c][(d+1) % 10] = val+1
            
            if combinations[(a-1) % 10][b][c][d] == -1 and str((a-1) % 10) + str(b) + str(c) + str(d) not in deadends:
                queue.append(((a-1) % 10, b, c, d, val+1))
                combinations[(a-1) % 10][b][c][d] = val+1
            if combinations[a][(b-1) % 10][c][d] == -1 and str(a) + str((b-1) % 10) + str(c) + str(d) not in deadends:
                queue.append((a, (b-1) % 10, c, d, val+1))
                combinations[a][(b-1) % 10][c][d] = val+1
            if combinations[a][b][(c-1) % 10][d] == -1 and str(a) + str(b) + str((c-1) % 10) + str(d) not in deadends:
                queue.append((a, b, (c-1)%10, d, val+1))
                combinations[a][b][(c-1) % 10][d] = val+1
            if combinations[a][b][c][(d-1) % 10] == -1 and str(a) + str(b) + str(c) + str((d-1) % 10) not in deadends:
                queue.append((a, b, c, (d-1) % 10, val+1))
                combinations[a][b][c][(d-1) % 10] = val+1
        return -1
        