class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        number_of_satisfied_without_ability = sum([customers[i] * (1 - grumpy[i]) for i in range(n)])
        print(number_of_satisfied_without_ability)
        
        ability_gain = sum([customers[i] * (grumpy[i]) for i in range(minutes)])
        max_ability_gain = ability_gain
        for i in range(0, n - minutes):
            ability_gain -= customers[i] * grumpy[i]
            ability_gain += customers[i+minutes] * grumpy[i+minutes]
            max_ability_gain = max(max_ability_gain, ability_gain)

        return number_of_satisfied_without_ability + max_ability_gain
        