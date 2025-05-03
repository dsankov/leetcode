class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        for first_value in [tops[0], bottoms[0]]:
            if all(first_value in domino for domino in zip(tops, bottoms)):
                max_same_oriented = max(tops.count(first_value), bottoms.count(first_value))
                return len(tops) - max_same_oriented
        return -1
        