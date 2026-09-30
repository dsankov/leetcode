class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split(sep="/")
        result_path = []
        for folder in dirs:
            if not folder or folder == ".":
                continue
            if folder == "..":
                if result_path:
                    result_path.pop()
                continue
            result_path.append(folder)
        result = "/" + "/".join(result_path)
        return result
        