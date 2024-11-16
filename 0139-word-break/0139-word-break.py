class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        word_dict = set(wordDict)
        dp = [None] * (n + 1)
        dp[n] = True

        def rec(start_word):
            if dp[start_word] is not None:
                return dp[start_word]
            
            for end_word in range(start_word, n):
                if s[start_word: end_word+1] in word_dict:
                    if rec(end_word+1):
                        dp[start_word] = True
                        return dp[start_word]
            dp[start_word] = False
            return dp[start_word]

        return rec(0)
            