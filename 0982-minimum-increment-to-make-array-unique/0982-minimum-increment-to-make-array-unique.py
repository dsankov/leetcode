class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums_counter = Counter(nums)
        nums_list = sorted(nums_counter)
        last_seen_num = nums_list[0]-1
        result = 0
        carry = 0
        # print(f"{nums_list=} {nums_counter=}")
        for num in nums_list:
            slot_lenght = num - last_seen_num - 1
            # print(f"Enter cycle: {result=} {carry=} {last_seen_num=} {num=} {slot_lenght=}")
            if carry <= slot_lenght:

                result += carry * (carry+1) // 2
                carry = 0
                # print(f"\t empty carry: {result=} {carry=}")
            else:
                result += slot_lenght * (slot_lenght + 1) // 2
                carry -= slot_lenght
                result += carry * (slot_lenght + 1)
                # print(f"\t pass carry: {result=} {carry=}")
            carry += nums_counter[num] - 1
            last_seen_num = num
            # print(f"\t leave cycle: {result=} {carry=} {last_seen_num=}")


        result += carry * (carry+1) // 2
        return result
        