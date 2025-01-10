class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        letter_counters_1 = [Counter(word) for word in words1]
        letter_counters_2 = [Counter(word) for word in words2]

        max_freqs_2 = defaultdict(int)
        for i in range(len(words2)):
            for ch, count in letter_counters_2[i].items():
                max_freqs_2[ch] = max(max_freqs_2[ch], count) 
        result = []

        for i, word in enumerate(words1):
            letter_counter = letter_counters_1[i]
            for ch, count in max_freqs_2.items():
                if letter_counter[ch] < count:
                    break
            else:
                result.append(word)

        return result

        