class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
        for folder in path:
            if folder:
                print(folder)
                if folder == "..":
                    if stack:
                        stack.pop()
                elif folder == ".":
                    continue
                else:
                    stack.append(folder)
        return "/" + "/".join(stack)