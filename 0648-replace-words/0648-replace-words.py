class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=lambda x: len(x))
        words = sentence.split()
        n = len(words)
        for i in range(n):
            for root in dictionary:
                if words[i].startswith(root):
                    words[i] = root
                    break
                    
        result = " ".join(words)
        return result
        
        