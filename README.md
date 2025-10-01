# Max Heap Implementation (Python)

This project implements a **Max Heap** in Python from scratch.  
A Max Heap is a **binary heap** where the **parent node is always greater than or equal to its children**, making it useful for priority queues and sorting algorithms.

---

## Features
- Insert elements while maintaining the **Max Heap property**.
- Remove the maximum element efficiently (`pop` operation).
- Heap automatically rearranges elements after insertion or removal.
- Fully implemented **heapify up** and **heapify down** without using built-in heap libraries.
- Supports easy printing of heap contents for visualization.

---

## Example Usage

```python
heap = Maxheap()
numbers = [5, 3, 8, 1, 2, 7, 9, 4, 6]

print("Inserting numbers:", numbers)
for num in numbers:
    heap.insert(num)
    print(f"After inserting {num}: {heap}")

print("\nPopping elements in descending order:")
while heap.heap:
    print(heap.pop(), end=" ")

Sample Output

Inserting numbers: [5, 3, 8, 1, 2, 7, 9, 4, 6]
After inserting 5: [5]
After inserting 3: [5, 3]
After inserting 8: [8, 3, 5]
After inserting 1: [8, 3, 5, 1]
After inserting 2: [8, 3, 5, 1, 2]
After inserting 7: [8, 3, 7, 1, 2, 5]
After inserting 9: [9, 8, 7, 1, 2, 5, 3]
After inserting 4: [9, 8, 7, 4, 2, 5, 3, 1]
After inserting 6: [9, 8, 7, 4, 6, 5, 3, 1, 2]

Popping elements in descending order:
9 8 7 6 5 4 3 2 1
