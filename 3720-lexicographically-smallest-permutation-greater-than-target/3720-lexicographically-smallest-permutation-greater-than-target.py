class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)

        cnt = [0] * 26

        for c in s:
            cnt[ord(c) - ord('a')] += 1

        # prefix = part that currently matches target
        prefix = []

        for i in range(n):

            x = ord(target[i]) - ord('a')

            # If target[i] is unavailable,
            # we cannot continue matching.
            if cnt[x] == 0:
                break

            cnt[x] -= 1
            prefix.append(target[i])

        # If we stopped before matching the whole target (because the
        # needed character ran out), first try placing a character
        # strictly greater than target[i] right at that same position,
        # using whatever counts are left (nothing was consumed here yet).
        if len(prefix) < n:
            i = len(prefix)
            x = ord(target[i]) - ord('a')

            for c in range(x + 1, 26):
                if cnt[c] == 0:
                    continue

                ans = "".join(prefix) + chr(ord('a') + c)

                cnt[c] -= 1

                for ch in range(26):
                    ans += chr(ord('a') + ch) * cnt[ch]

                return ans

        # Otherwise (or if that attempt failed), backtrack through the
        # matched prefix from right to left.
        for i in range(len(prefix) - 1, -1, -1):

            # Restore the character at position i.
            cnt[ord(prefix[i]) - ord('a')] += 1
            prefix.pop()

            x = ord(target[i]) - ord('a')

            # Find smallest character > target[i].
            for c in range(x + 1, 26):

                if cnt[c] == 0:
                    continue

                ans = "".join(prefix) + chr(ord('a') + c)

                cnt[c] -= 1

                # Fill remaining characters in sorted order.
                for ch in range(26):
                    ans += chr(ord('a') + ch) * cnt[ch]

                return ans

        return ""