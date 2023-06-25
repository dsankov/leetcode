class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        skip_s = skip_t = 0
        
        
        while i >= 0 or j >= 0:
            s_char = None
            while i >= 0: 
                if s[i] == "#":
                    skip_s += 1
                elif skip_s > 0:
                    skip_s -= 1
                else:
                    s_char = s[i]
                    break
                i -= 1

            t_char = None
            while j >= 0:
                if t[j] == "#":
                    skip_t += 1
                elif skip_t > 0:
                    skip_t -= 1
                else:
                    t_char = t[j]
                    break
                j -= 1

            if s_char != t_char:
                return False
            else:
                i -= 1
                j -= 1  
        
        return True    
                
