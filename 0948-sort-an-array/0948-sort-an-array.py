class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # self.bubble_sort(nums)
        # self.selection_sort(nums)
        # self.insertion_sort(nums)
        # self.merge_sort(nums)
        # self.heap_sort(nums)

        # Time limit error
        self.quick_sort(nums)


        return nums
    def merge_sort(self, nums): 
        if len(nums) <= 1:
            return

        mid = len(nums)//2
        left_part = nums[:mid] 
        right_part = nums[mid:] 

        self.merge_sort(left_part)
        self.merge_sort(right_part)

        def merge_sorted(left_part, right_part, nums):
            read_left, read_right, write_result = 0, 0 ,0

            while read_left < len(left_part) and read_right < len(right_part): 
                if left_part[read_left] < right_part[read_right]: 
                    nums[write_result] = left_part[read_left]
                    read_left += 1
                else: 
                    nums[write_result] = right_part[read_right] 
                    read_right += 1
                write_result += 1

            while read_left < len(left_part): 
                nums[write_result] = left_part[read_left] 
                read_left += 1
                write_result += 1

            while read_right < len(right_part): 
                nums[write_result] = right_part[read_right]
                read_right += 1
                write_result += 1

        merge_sorted(left_part, right_part, nums)

    def bubble_sort(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(n - 1 - i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

    def insertion_sort(self, nums):
        n = len(nums)
        for curr_position in range(1, n):
            curr_value = nums[curr_position]
            insert_position = curr_position
            while insert_position > 0 and nums[insert_position - 1] > curr_value:
                nums[insert_position] = nums[insert_position - 1]
                insert_position -= 1
            nums[insert_position] = curr_value

    def selection_sort(self, nums):
        n = len(nums)
        for write_min_index in range(n):
            min_index = write_min_index
            for read_index in range(write_min_index + 1, n):
                if nums[read_index] < nums[min_index]:
                    min_index = read_index
            nums[write_min_index], nums[min_index] = nums[min_index], nums[write_min_index] 

    def heap_sort(self, nums):
        nums_heap = []
        for num in nums:
            heappush(nums_heap, num)
        for i in range(len(nums)):
            nums[i] = heappop(nums_heap)

    def quick_sort(self, nums):
        def median_of_three(arr, low, high):
            mid = (low + high) // 2
            # Определяем медиану из элементов arr[low], arr[mid], arr[high]
            if arr[low] > arr[mid]:
                arr[low], arr[mid] = arr[mid], arr[low]
            if arr[low] > arr[high]:
                arr[low], arr[high] = arr[high], arr[low]
            if arr[mid] > arr[high]:
                arr[mid], arr[high] = arr[high], arr[mid]
            # Возвращаем индекс медианного элемента
            return mid

        def quick_sort_inplace(nums, left, right):
            if left >= right:
                return

            # pivot_index = median_of_three(nums, left, right)
            pivot_index = left
            pivot = nums[pivot_index]
            less_than_pivot_ptr = left -1
            greater_than_pivot_ptr = right + 1
            current_ptr = left
            while current_ptr < greater_than_pivot_ptr:
                if nums[current_ptr] < pivot:
                    less_than_pivot_ptr += 1
                    nums[less_than_pivot_ptr] , nums[current_ptr] = nums[current_ptr], nums[less_than_pivot_ptr]
                    current_ptr += 1
                elif nums[current_ptr] > pivot:
                    greater_than_pivot_ptr -= 1
                    nums[greater_than_pivot_ptr], nums[current_ptr] = nums[current_ptr], nums[greater_than_pivot_ptr]
                else:
                    current_ptr += 1


            quick_sort_inplace(nums, left, less_than_pivot_ptr)
            quick_sort_inplace(nums, greater_than_pivot_ptr, right)
            
        
        
        
        
        
        def partition(nums, low, high):
            pivot_index = median_of_three(nums, low, high)
            pivot = nums[pivot_index]
            nums[pivot_index], nums[high] = nums[high], nums[pivot_index]
            i = low - 1
            for j in range(low, high):
                if nums[j] <= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i + 1], nums[high] = nums[high], nums[i + 1]
            return i + 1

        quick_sort_inplace(nums, 0, len(nums)-1)

        
