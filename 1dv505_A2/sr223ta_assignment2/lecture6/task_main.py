



from Heap import Heap
from Task import Task


print("Task demo with priority queue starts\n")
heap = Heap()


tasks = [
    Task(100, "Give mom a hug!"),
    Task(77, "Feed the dog"),
    Task(50, "Finish assignment 2"),
    Task(90, "Compute physic"),
    Task(20, "Meet family memmber"),
    Task(10, "Go to bed early"),
    Task(30, "Eat outside with a friend"),
    Task(70, "Scroll TikTok"),
    Task(60, "Go to Gym"),
    Task(80, "Eat more protein"),
]

print("Adding tasks to heap:")
for task in tasks:
    heap.add(task)
    print(f"Added: {task}")

print("\nProcessing tasks in priority order:")
while not heap.is_empty():
    print(heap.pull_high())
