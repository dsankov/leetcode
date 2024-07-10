class Solution:
    def minOperations(self, logs: List[str]) -> int:
        level = 0
        for command in logs:
            if command.startswith("./"):
                continue
            if command.startswith(".."):
                if level > 0:
                    level -= 1
                continue
            level += 1
        return level
        