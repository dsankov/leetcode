MX = 1_000_001
factors = [[] for _ in range(MX)]
for i in range(2, MX):
    if not factors[i]:
        for j in range(i, MX, i):
            factors[j].append(i)


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        edges = defaultdict(list)
        for i, a in enumerate(nums):
            for p in factors[a]:
                edges[p].append(i)
        res = 0
        seen = [False] * n
        seen[0] = True
        q = [0]
        while True:
            q2 = []
            for i in q:
                if i == n - 1:
                    return res
                if i > 0 and not seen[i - 1]:
                    seen[i - 1] = True
                    q2.append(i - 1)
                if i < n - 1 and not seen[i + 1]:
                    seen[i + 1] = True
                    q2.append(i + 1)
                if len(factors[nums[i]]) == 1:
                    p = nums[i]
                    for j in edges[p]:
                        if not seen[j]:
                            seen[j] = True
                            q2.append(j)
                    edges[p].clear()
            q = q2
            res += 1
            
# MAX_NUM = 10 ** 6 + 1
# is_prime = [True] * MAX_NUM
# is_prime[0] = is_prime[1] = False
# divisors = defaultdict(list)
# for num in range(2, MAX_NUM):
#     if not is_prime[num]:
#         continue
#     divisors[num].append(num)
#     for multiple in range(2 * num, MAX_NUM, num):
#         is_prime[multiple] = False
#         divisors[multiple].append(num)
    
# class Solution:
#     def minJumps(self, nums: List[int]) -> int:
#         n = len(nums)

#         primes_lists = defaultdict(list)
#         for i, num in enumerate(nums):
#             if is_prime[num]:
#                 primes_lists[num].append(i)

#         adjacents = defaultdict(set)
#         for i, num in enumerate(nums):
#             if i > 0:
#                 adjacents[i].add(i - 1)
#             if i < n - 1:
#                 adjacents[i].add(i + 1)

#             for prime_div in divisors[num]:
#                 for prime_idx in primes_lists[prime_div]:
#                     if prime_idx != i:
#                         adjacents[prime_idx].add(i)

#         idx_queue = deque()
#         idx_queue.append(0)
#         visited = [False] * n
        
#         step = -1
#         while idx_queue:
#             step += 1
#             level_size = len(idx_queue)
#             while level_size > 0:
#                 level_size -= 1
#                 cur_idx = idx_queue.popleft()
#                 visited[cur_idx] = True
#                 if cur_idx == n - 1:
#                     return step
#                 for adj_idx in adjacents[cur_idx]:
#                     if not visited[adj_idx]:
#                         idx_queue.append(adj_idx)

#         return step
        