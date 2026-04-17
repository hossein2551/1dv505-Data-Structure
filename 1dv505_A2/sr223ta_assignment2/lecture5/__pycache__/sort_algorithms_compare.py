




import random

import time



from sort_algorithms import selection_sort, bubble_sort, insertion_sort


def generate_random_list(size):

    return [random.randint(0, 1000) for _ in range(size)]


def evaluate_performance(sort_function, arr):

    start_time = time.perf_counter()

    sort_function(arr)

    return time.perf_counter() - start_time



arr_size = 10000

arr = generate_random_list(arr_size)



selection_arr = arr.copy()

bubble_arr = arr.copy()

insertion_arr = arr.copy()




selection_time = evaluate_performance(selection_sort, selection_arr)

bubble_time = evaluate_performance(bubble_sort, bubble_arr)

insertion_time = evaluate_performance(insertion_sort, insertion_arr)



print(f"Selection Sort Time: {selection_time:.6f} seconds")

print(f"Bubble Sort Time: {bubble_time:.6f} seconds")

print(f"Insertion Sort Time: {insertion_time:.6f} seconds")




print("\nComparison of Sorting Algorithms:")

print(f"Fastest: {'Selection Sort' if selection_time < bubble_time and selection_time < insertion_time else 'Bubble Sort' if bubble_time < insertion_time else 'Insertion Sort'}")


print(f"Slowest: {'Bubble Sort' if bubble_time > selection_time and bubble_time > insertion_time else 'Selection Sort' if selection_time > insertion_time else 'Insertion Sort'}")