import matplotlib.pyplot as plt
import time
import random


def measure_execution_time(func, lst):
    start = time.time()
    func(lst)
    end = time.time()
    return end - start


def threesum_brute(lst, target=0):
    unique_triples = set()
    n = len(lst)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if lst[i] + lst[j] + lst[k] == target:
                    triple = tuple(sorted([lst[i], lst[j], lst[k]]))
                    unique_triples.add(triple)
    return list(unique_triples)

input_sizes = list(range(100, 600, 100))
times = {1: [], 2: [], 3: []}


for size in input_sizes:
    random_list = [random.randint(-10*size, 10*size) for _ in range(size)]
    for run in range(1, 4):
        elapsed = measure_execution_time(threesum_brute, random_list)
        times[run].append(elapsed)


plt.figure(figsize=(10, 6))
for run in range(1, 4):
    random_list = [random.randint(-10 * size, 10 * size) for _ in range(size)]
    run_times = [measure_execution_time(threesum_brute, random_list) for size in input_sizes]
    plt.plot(input_sizes, run_times, label=f'Run {run}')

plt.title('Execution Time for 3-Sum Brute Force')
plt.xlabel('Input List Size')
plt.ylabel('Execution Time (seconds)')
plt.legend()
plt.grid()
plt.show()