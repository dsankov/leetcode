class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        task_pq = [(-num_to_do, task) for task, num_to_do in Counter(tasks).items()]
        heapify(task_pq)
        waiting_queue = deque()
        time = 0

        while task_pq or waiting_queue:
            if waiting_queue and waiting_queue[0][2] <= time:
                next_task, num_to_do, min_usage_time = waiting_queue.popleft()
                heappush(task_pq, (-num_to_do, next_task))

            if task_pq:
                neg_num, curr_task = heappop(task_pq)
                num_to_do = -neg_num
                num_to_do -= 1
                if num_to_do > 0:
                    waiting_queue.append((curr_task, num_to_do, time + n + 1))

            time += 1

        return time
        