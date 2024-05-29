class Solution:
    def numSteps(self, s: str) -> int:
        s = list(s[::-1])
        current_lenght = len(s)
        s.append("0")

        start = 0
        steps_count = 0
    
        while current_lenght != 1:
            steps_count += 1
            if s[start] == "0":
                start += 1
                current_lenght -= 1
            else:
                i = 0 
                while s[start+i] == "1":
                    s[start+i] = "0"
                    i += 1
                s[start+i] = "1"
                current_lenght = max(current_lenght, i+1)
            
        return steps_count
        