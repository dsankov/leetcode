class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        # n = len(s)
        char_count = collections.Counter(s)
        prefix = []

        for target_char in target:
            if char_count[target_char] == 0:
                break

            char_count[target_char] -= 1
            prefix.append(target_char)

        if len(prefix) < len(target):
            char_to_change = target[len(prefix)]
            char_to_change_idx = ord(char_to_change) - ord("a")

            for candidate_char in string.ascii_lowercase[char_to_change_idx + 1:]: 
                if char_count[candidate_char] == 0:
                    continue

                char_count[candidate_char] -= 1
                suffix = []
                for fill_char in string.ascii_lowercase:
                    suffix.append(fill_char * char_count[fill_char])

                return "".join(prefix) + candidate_char + "".join(suffix)

        # Otherwise (or if that attempt failed), backtrack through the
        # matched prefix from right to left.

        # for i in range(len(prefix) - 1, -1, -1):
        for prefix_char in reversed(prefix):

            # Restore the character at position i.
            # cnt[ord(prefix[i]) - ord('a')] += 1
            char_count[prefix_char] += 1
            prefix.pop()

            # x = ord(target[i]) - ord('a')
            char_to_change_idx = ord(prefix_char) - ord("a")

            # Find smallest character > target[i].
            for candidate_char in string.ascii_lowercase[char_to_change_idx + 1:]: 
                if char_count[candidate_char] == 0:
                    continue

                char_count[candidate_char] -= 1
                suffix = []
                for fill_char in string.ascii_lowercase:
                    suffix.append(fill_char * char_count[fill_char])

                return "".join(prefix) + candidate_char + "".join(suffix)

        return ""