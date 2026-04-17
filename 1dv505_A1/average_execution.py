

import matplotlib.pyplot as plt
import time
import random

from tre_separate_runs import measure_execution_time, threesum_brute



input_sizes = list(range(100, 600, 100))
times = {size: [] for size in input_sizes}


for size in input_sizes:
    random_list = [random.randint(-10 * size, 10 * size) for _ in range(size)]
    time_measurements = []
    time_measurements = [measure_execution_time(threesum_brute, random_list) for _ in range(5)]
    average_time = sum(time_measurements) / len(time_measurements)
    times[size]= average_time

plt.figure(figsize=(10, 6))
plt.plot(input_sizes, [times[size] for size in input_sizes], label='Average Execution Time')
plt.title('Average Execution Time for 3-Sum Brute Force')
plt.xlabel('Input List Size')
plt.ylabel('Average Execution Time (seconds)')
plt.legend()
plt.grid()
plt.show()