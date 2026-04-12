# import string

# class Solution:
#     def minimumDistance(self, word: str) -> int:
#         word = " " + word
#         def dist(a: str, b:str) -> int:
#             if a == " " or b == " ":
#                 return 0
#             a = ord(a) - ord("A")
#             b = ord(b) - ord("A")
#             return abs(a//6 - b//6) + abs(a%6 - b%6)

#         cur_hand = {char : 0 for char in string.ascii_uppercase}
        
#         for idx, char in enumerate(word):
#             next_hand = dict.fromkeys(string.ascii_uppercase, 0)
#             cur_char = word[i]
#             next_char = word[i+1]
#             for temp_char in cur_hand:
#                 cur_hand[left_char] = min(
#                     left_hand[left_char], 
#                     right_hand[left_char] + dist(left_char, char))

#         result = 0

#         return result
        
class Solution:
    def minimumDistance(self, word: str) -> int:

        def dist(a,b):
            if a==26 or b==26:
                return 0
            return abs(a//6-b//6)+abs(a%6-b%6)

        n=len(word)
        INF=10**9

        dp=[[[INF]*27 for _ in range(27)] for _ in range(n+1)]
        dp[0][26][26]=0

        for i in range(n):
            cur=ord(word[i])-65

            for f1 in range(27):
                for f2 in range(27):
                    val=dp[i][f1][f2]
                    if val==INF: continue

                    dp[i+1][cur][f2]=min(
                        dp[i+1][cur][f2],
                        val+dist(f1,cur)
                    )

                    dp[i+1][f1][cur]=min(
                        dp[i+1][f1][cur],
                        val+dist(f2,cur)
                    )

        return min(
            dp[n][i][j]
            for i in range(27)
            for j in range(27)
        )