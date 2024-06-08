class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        n = len(words)
        letters = {}
        common_letters = defaultdict(int)
        for word in words:
            letters[word] = Counter(word)
        for letter in letters[words[0]]:
            common_letters[letter] = letters[words[0]][letter]
            for word in words:
                if letter in letters[word]:
                    common_letters[letter] = min(common_letters[letter], letters[word][letter])
                else:
                    common_letters[letter] = 0

        result = []
        for letter, number in common_letters.items():
            result.extend(letter * number)
        return result