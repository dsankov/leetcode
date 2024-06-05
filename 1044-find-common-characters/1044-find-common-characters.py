class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        n = len(words)
        letters = {}
        result = defaultdict(int)
        for word in words:
            letters[word] = Counter(word)
        # print(letters)
        for letter in letters[words[0]]:
            result[letter] = letters[words[0]][letter]
            # print(letter)
            for word in words:
                if letter in letters[word]:
                    # print(letters[words[0]][letter], letters[word][letter])
                    result[letter] = min(result[letter], letters[word][letter])
                else:
                    result[letter] = 0

        # print(result)
        answer = []
        for letter, number in result.items():
            answer.extend(letter * number)
        return answer