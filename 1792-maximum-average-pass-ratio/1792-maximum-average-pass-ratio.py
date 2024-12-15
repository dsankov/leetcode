class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        def get_gain(class_pass, class_total):
            return (class_pass+1) / (class_total+1) - class_pass / class_total
        
        classes_queue = [(-get_gain(class_pass, class_total), class_pass, class_total) for class_pass, class_total in classes]
        heapify(classes_queue)

        for _ in range(extraStudents):
            _, curr_pass, curr_total = heappop(classes_queue)
            heappush(classes_queue, (-get_gain(curr_pass + 1, curr_total + 1), curr_pass+1, curr_total+1))

        return sum((class_pass / class_total) for _, class_pass, class_total in classes_queue) / len(classes)

        
