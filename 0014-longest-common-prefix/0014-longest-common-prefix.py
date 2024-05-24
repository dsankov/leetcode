class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        min_lenght = min([len(string) for string in strs])
        common_prefix = ""
        diff_detected = False

        for i in range(min_lenght):
            ch = strs[0][i]
            for j in range(1, n):
                if strs[j][i] != ch:
                    diff_detected = True
                    break
            if diff_detected:
                return common_prefix
            common_prefix += ch
        return common_prefix           