class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        open_brackets = []
        unlocked_symbols = []

        for idx, (char, status) in enumerate(zip(s, locked)):
            if status == "0":
                unlocked_symbols.append(idx)
            elif char == "(":
                open_brackets.append(idx)
            elif char == ")":
                if open_brackets:
                    open_brackets.pop()
                elif unlocked_symbols:
                    unlocked_symbols.pop()
                else:
                    return False

        while (open_brackets and unlocked_symbols
               and open_brackets[-1] < unlocked_symbols[-1]):
               open_brackets.pop()
               unlocked_symbols.pop()

        if open_brackets:
            return False

        return True