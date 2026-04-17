

import pytest

from sort_algorithms import selection_sort, bubble_sort, insertion_sort
from quick_merge import merge_sort, quick_sort



sorting_algorithms = {
    "Selection Sort": selection_sort,
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort
}


test_cases = [
    [],  
    [1],  
    [5, 2, 9, 1, 5, 6],  
    [1, 2, 3, 4, 5],  
    [5, 4, 3, 2, 1], 
    [1, 3, 2, 3, 1],  
]

def test_sorting_algorithms():
    for name, sorting_function in sorting_algorithms.items():
        for test_case in test_cases:
            input_list = test_case[:]
            sorted_output = sorting_function(input_list)
            

            if sorted_output != sorted(test_case):
                print(f"The test failed for {name} with input {test_case}")
            else:
                print(f"The test succssed for {name} with input {test_case}")
