class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keymap = {             "2": "abc", "3": "def", 
                  "4": "ghi",  "5": "jkl", "6": "mno",
                  "7": "pqrs", "8": "tuv", "9": "wxyz"
                  }
        if not digits:
            return []

        def bfs(digits: str) -> List[str]:
            if not digits:
                return [""]
            first_digit = digits[0]
            tail_list = bfs(digits[1:])
            result = []
            for tail in tail_list:
                for char in keymap[first_digit]:
                    result.append(char+tail)
            return result
        return bfs(digits)