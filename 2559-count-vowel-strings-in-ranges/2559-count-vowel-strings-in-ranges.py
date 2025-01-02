class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        prefix_sums = [0] * (len(words) + 1)
        for i, word in enumerate(words):
            prefix_sums[i+1] = prefix_sums[i] + (1 if word[0] in vowels and word[-1] in vowels else 0)

        result = []
        for start, end in queries:
            result.append(prefix_sums[end+1] - prefix_sums[start])
        return result
