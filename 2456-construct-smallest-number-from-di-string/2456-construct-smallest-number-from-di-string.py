from itertools import permutations

class Solution:
    def smallestNumber(self, pattern: str) -> str:

        def lexicographical_permutations(iterable):
            # sorted_arr = sorted(arr)
            # return permutations(sorted_arr)

            sorted_arr = sorted(iterable)
            yield sorted_arr
            while next_permutation(sorted_arr):
                yield sorted_arr

        def next_permutation(arr):
            i = len(arr) - 2
            while i >= 0 and arr[i] >= arr[i+1]:
                i -= 1
            if i == -1:
                return False
            
            j = len(arr) - 1
            while arr[i] >= arr[j]:
                j -= 1
            # default j := i + 1
            arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1:] = reversed(arr[i + 1:])
            return True


        def check_pattern(perm, pattern):
            for i in range(len(pattern)):
                if not (
                    perm[i] < perm[i+1] and pattern[i] == "I"
                    or perm[i] > perm[i+1] and pattern[i] == "D"
                ):
                    
                    return False
            return True

        for perm in lexicographical_permutations("123456789"[:len(pattern) + 1]):
            if check_pattern(perm, pattern):
                return "".join(perm)
        return ""