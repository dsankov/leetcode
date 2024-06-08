class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        counted_cards = Counter(hand)
        while counted_cards:
            start_card = min(counted_cards)
            for i in range(groupSize):
                if start_card + i not in counted_cards:
                    return False
                counted_cards[start_card+i] -= 1
                if counted_cards[start_card+i] == 0:
                    counted_cards.pop(start_card+i)

        return True