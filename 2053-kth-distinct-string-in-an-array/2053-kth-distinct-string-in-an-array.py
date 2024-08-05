class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        for  string, frequency in Counter(arr).items():
            if frequency == 1:
                k -= 1
            if k == 0:
                return string
        return ""