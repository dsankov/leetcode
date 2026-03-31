class Solution:
    def generateString(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        word = [""] * (n + m - 1)
        fixed = [False] * (n + m - 1)
        t = list(t)
        print(t)

        for i, flag in enumerate(s):
            if flag == "F":
                continue
            
            for j, letter in enumerate(t):
                if word[i+j] and word[i+j] != letter:
                    return ""
                word[i+j] = letter
                fixed[i+j] = True

        word = [letter if letter else "a" for letter in word]
        for i, flag in enumerate(s):
            if flag == "T":
                continue
            if word[i: i + m] != t:
                continue
            if all(fixed[i: i + m]):
                return ""
            
            for j in range(i + m -1, i - 1, -1):
                if fixed[j]:
                     continue
                temp_letter = word[j]
                if ord(temp_letter) == ord("z"):
                    return ""
                next_letter = str(ord(temp_letter) + 1)
                word[j] = next_letter  
                break
            else:
                return ""

        return "".join(word)
        