

import math
import matplotlib.pyplot as plt
import time
import random

from tre_separate_runs import measure_execution_time, threesum_brute


input_sizes = list(range(100, 600, 100))
times = {}

for size in input_sizes:
    random_list = [random.randint(-10 * size, 10 * size) for _ in range(size)]
    time_measurements = [measure_execution_time(threesum_brute, random_list) for _ in range(5)]
    average_time = sum(time_measurements) / len(time_measurements)
    times[size] = average_time


log_sizes = [math.log(size) for size in input_sizes]
log_times = [math.log(times[size]) for size in input_sizes]


n = len(log_sizes)
mean_x = sum(log_sizes) / n
mean_y = sum(log_times) / n

numerator = sum((log_sizes[i] - mean_x) * (log_times[i] - mean_y) for i in range(n))
denominator = sum((log_sizes[i] - mean_x) ** 2 for i in range(n))

slope = numerator / denominator  
intercept = mean_y - slope * mean_x


print(f"Beräknad tidskomplexitet: O(n^{slope:.2f})")

plt.figure(figsize=(10, 6))
plt.scatter(log_sizes, log_times, color='red', label='Data')
plt.plot(log_sizes, [slope * x + intercept for x in log_sizes], color='green', label=f"Regression: O(n^{slope:.2f})")
plt.xlabel('Log(Input Size)')
plt.ylabel('Log(Execution Time)')
plt.title('Tidskomplexitet: Log-Log Plot')
plt.legend()
plt.grid()
plt.show()