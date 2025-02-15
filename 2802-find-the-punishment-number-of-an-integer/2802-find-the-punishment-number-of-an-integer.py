class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_partition(str_num: str, target: int) -> bool:
            if not str_num and target == 0:
                return True
            if target < 0:
                return False
            
            for split_pos in range(1, len(str_num) + 1):
                left_part = str_num[:split_pos]
                left_num = int(left_part)
                right_part = str_num[split_pos:]
                if can_partition(right_part, target - left_num):
                    return True
            return False
        
        punishment = 0
        for num in range(1, n + 1):
            if can_partition(str(num ** 2), num):
                punishment += num ** 2
        return punishment
