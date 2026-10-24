class Solution:
    def simplifyPath(self, path: str) -> str:
        clean_elements = []
        path = path[1:]
        while path != "":
            first_slash = path.find("/")
            if first_slash == -1:
                clean_elements.append(path)
                break
            elif path[:first_slash] == "":
                path = path[first_slash+1:]
            else:
                clean_elements.append(path[:first_slash])
                path = path[first_slash+1:]
        stk = []
        for el in clean_elements:
            if el == "..":
                stk.pop() if stk else None
            elif el == ".":
                continue
            else:
                stk.append(el)
        return "/" + "/".join(stk)
                

