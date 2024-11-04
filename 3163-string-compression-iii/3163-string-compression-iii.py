class Solution:
    def compressedString(self, word: str) -> str:
        comp = []
        count = 1
        prev_char = word[0]
        for char in word[1:]:
            if char == prev_char:
                count += 1
                if count > 9:
                    comp.append("9" + char)
                    count = 1
            else:
                comp.append(f"{count}{prev_char}")
                prev_char = char
                count = 1
        comp.append(f"{count}{prev_char}")
        return "".join(comp)
        