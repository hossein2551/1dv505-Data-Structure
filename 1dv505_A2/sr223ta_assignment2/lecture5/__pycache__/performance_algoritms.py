


import time
import random

import matplotlib.pyplot as plt


from quick_merge import merge_sort, quick_sort 


sizes = [10000, 30000, 60000, 90000, 120000, 150000]


runs = 5


merge_times = []

quick_times = []


for size in sizes:


    total_merge_time = 0

    total_quick_time = 0



    for _ in range(runs): 


        random_lsit = [random.randint(0, 10000) for _ in range(size)]

        
        start = time.time()

        merge_sort(random_lsit)

        total_merge_time += time.time() - start

        
        start = time.time()

        quick_sort(random_lsit)

        total_quick_time += time.time() - start

    
    merge_times.append(total_merge_time / runs)


    quick_times.append(total_quick_time / runs)

plt.figure(figsize=(10, 6))

plt.plot(sizes, merge_times, label="Merge Sort", marker='o')

plt.plot(sizes, quick_times, label="Quick Sort", marker='o')

plt.ylim(0, 0.025)

plt.yticks([0.000, 0.025, 0.050, 0.075, 0.100, 0.125, 0.150, 0.175, 0.2000])


plt.xlabel("List Sizes in range 10000 to 150000")

plt.ylabel("Average Time (seconds)")

plt.title("Running times for n * log(n) algorithms")

plt.legend()


plt.show()                                          
