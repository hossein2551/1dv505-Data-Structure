



from Heap import Heap


print("Heap demo starts\n")
heap = Heap()


print("Adding elements to heap...")
for elem in [10, 20, 5, 3, 30, 25]:
    heap.add(elem)
    print(f"Added: {elem}")
print("Heap content:", heap)

print("\nHighest element (peek):", heap.peek())

print("\nRemoving the highest element...")
print("Removed:", heap.pull_high())
print("Heap content after removal:", heap)

print("\nIs heap empty?", heap.is_empty())


print("\nIterating through heap elements:")
for value in heap:
    print(value, end=" ")
print()
