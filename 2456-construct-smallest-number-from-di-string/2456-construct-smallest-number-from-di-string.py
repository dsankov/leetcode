from itertools import permutations

class Solution:
    def smallestNumber(self, pattern: str) -> str:

        def lexicographical_permutations(iterable):
            sorted_iterable = sorted(iterable)
            return permutations(sorted_iterable)

        def check_pattern(perm, pattern):
            for i in range(len(pattern)):
                if perm[i] < perm[i+1] and pattern[i] == "I":
                    continue
                if perm[i] > perm[i+1] and pattern[i] == "D":
                    continue
                return False
            return True

        for perm in lexicographical_permutations("123456789"):
            if check_pattern(perm, pattern):
                return "".join(perm[:len(pattern)+1])
        return ""