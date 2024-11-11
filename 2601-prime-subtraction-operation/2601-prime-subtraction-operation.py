class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        n = len(nums)
        max_num = max(nums)
        
        sieve = [True] * (max_num + 1)
        sieve[1] = False    # But sieve[0] = True 
        for num in range(2, max_num + 1):
            if sieve[num]:
                for not_prime in range(num * num, max_num + 1, num):
                    sieve[not_prime] = False
        
        value_to_place = 0
        for i in range(n):
            value_to_place += 1
            if nums[i] < value_to_place:
                return False
            while not sieve[ nums[i] - value_to_place ]:    # Prime or zero
                if nums[i] < value_to_place:
                    return False
                value_to_place += 1

        return True
            




        