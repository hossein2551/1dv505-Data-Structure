



import random

import time

import matplotlib.pyplot as plt

import math


from sort_algorithms import selection_sort, bubble_sort, insertion_sort

from sort_algorithms_compare import generate_random_list, evaluate_performance



def perform_linear_regression(x, y):
    
    n = len(x)

    sum_x = sum(x)

    sum_y =  sum(y)

    sum_xy = sum(x[i] * y[i] for i in range(n))

    sum_x_squard = sum(xi ** 2 for xi in x)

    slope = (n * sum_xy - sum_x *  sum_y) / (n * sum_x_squard - sum_x **2)

    intercept = (sum_y - slope * sum_x) / n


    return slope, intercept


sizes = [100, 200, 400, 800, 1600, 3200, 6400]  

selection_times = []

bubble_times = []

insertion_times = []

for size in sizes:

    arr = generate_random_list(size)

    selection_arr = arr.copy()

    bubble_arr = arr.copy()

    insertion_arr = arr.copy()
    
    
    
    selection_times.append(evaluate_performance(selection_sort, selection_arr))

    bubble_times.append(evaluate_performance(bubble_sort, bubble_arr))

    insertion_times.append(evaluate_performance(insertion_sort, insertion_arr))




log_sizes = [math.log(size) for size in sizes]

log_selection_times = [math.log(time) for time in selection_times]

log_bubble_times = [math.log(time) for time in bubble_times]

log_insertion_times = [math.log(time) for time in insertion_times]





selection_slope, _ = perform_linear_regression(log_sizes, log_selection_times)

bubble_slope, _ = perform_linear_regression(log_sizes, log_bubble_times)

insertion_slope, _ = perform_linear_regression(log_sizes, log_insertion_times)



plt.figure(figsize=(10, 6))

plt.loglog(sizes, selection_times, label = f"Selection Sort (k= {selection_slope:.2f})", marker='+', linestyle = ' ')

plt.loglog(sizes, bubble_times, label=f"Bubble Sort(k= {bubble_slope:.2f})", marker='+', linestyle = ' ')

plt.loglog(sizes, insertion_times, label = f"Insertion Sort(k = {insertion_slope:.2f})", marker='+', linestyle = ' ')



log_sizes = [math.log(size) for size in sizes]

log_selection_times = [math.log(time) for time in selection_times]

log_bubble_times = [math.log(time) for time in bubble_times]

log_insertion_times = [math.log(time) for time in insertion_times]




plt.xlabel("log2 of list sizes")

plt.ylabel("log2 of sorting times")

plt.legend()

plt.title("Log-Log Plot for Selection, Bubble and Insertion Sort")

plt.show()


print(f"Selection Sort Complexity: O(n^{selection_slope:.2f})")

print(f"Bubble Sort Complexity: O(n^{bubble_slope:.2f})")

print(f"Insertion Sort Complexity: O(n^{insertion_slope:.2f})")



plt.figure(figsize=(10, 6))

plt.plot(log_sizes, log_selection_times, label="Selection Sort", marker='o')

plt.plot(log_sizes, log_bubble_times, label="Bubble Sort", marker='o')

plt.plot(log_sizes, log_insertion_times, label="Insertion Sort", marker='o')


plt.plot(log_sizes, [selection_slope * xi + math.log(selection_times[0]) for xi in log_sizes], '--', label="Selection Regression")

plt.plot(log_sizes, [bubble_slope * xi + math.log(bubble_times[0]) for xi in log_sizes], '--', label="Bubble Regression")

plt.plot(log_sizes, [insertion_slope * xi + math.log(insertion_times[0]) for xi in log_sizes], '--', label="Insertion Regression")


plt.xlabel("Log(Input Size)")

plt.ylabel("Log(Time)")

plt.legend()

plt.title("Linear Regression for Selection, Bubble and Insertion Sort")

plt.show() 