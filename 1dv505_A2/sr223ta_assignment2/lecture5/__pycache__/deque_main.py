

import Deque as deq



print("Deque demo starts\n")
deque = deq.Deque()


for i in range(1, 11):
    deque.add_last(i)
print(deque)
print("Size:", deque.size)


for i in range(11, 21):
    deque.add_first(i)
print(deque)
print("Size:", deque.size)


print("\nget_last():", deque.get_last())
print("get_first():", deque.get_first())
print("remove_first():", deque.remove_first())
print("remove_last():", deque.remove_last())
print(deque)
print("Size:", deque.size)
print("is_empty():", deque.is_empty())



print("\nTest to remove all elements")
deque = deq.Deque()   
for i in range(100, 106):
    deque.add_first(i)
print("After adding elements:", deque)

while not deque.is_empty():
    deque.remove_last()
print("After removing all elements:", deque)
print("Size:", deque.size)
print("is_empty():", deque.is_empty())


print("\nIterator test")
deque = deq.Deque()   
for i in range(1, 11):  
    deque.add_last(i)
for n in deque:
    print(n, end=" ")
print()


print("\nAccessing an empty deque")
empty = deq.Deque()     
try:
    empty.get_last()
except IndexError as exc:
    print("get_last:", exc)

try:
    empty.get_first()
except IndexError as exc:
    print("get_first:", exc)

try:
    empty.remove_first()
except IndexError as exc:
    print("remove_first:", exc)

try:
    empty.remove_last()
except IndexError as exc:
    print("remove_last:", exc)
