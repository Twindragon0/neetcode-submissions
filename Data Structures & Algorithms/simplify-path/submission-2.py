class Solution:
    def simplifyPath(self, path: str) -> str:
        new_els = []
        path = path[1:]
        while path != "":
            first_slash = path.find("/")
            if first_slash == -1:
                new_els.append(path)
                break
            substr = path[:first_slash]
            if substr == "":
                path = path[first_slash+1:]
            else:
                new_els.append(substr)
                path = path[first_slash+1:]
        stk = []
        for el in new_els:
            if el == ".":
                continue
            elif el == "..":
                stk.pop() if stk else None
            else:
                stk.append(el)
        return "/" + "/".join(stk)