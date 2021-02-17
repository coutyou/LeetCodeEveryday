class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split("/")
        stack = []
        for dir_ in dirs:
            if not dir_:
                pass
            elif dir_ == ".":
                pass
            elif dir_ == "..":
                if not stack:
                    pass
                else:
                    stack.pop()
            else:
                stack.append(dir_)
        return "/" + "/".join(stack)