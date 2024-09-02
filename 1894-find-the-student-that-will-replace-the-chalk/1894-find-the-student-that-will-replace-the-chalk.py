class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        return bisect_right([*accumulate(chalk)], k % sum(chalk))