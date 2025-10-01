class Maxheap:
    def __init__(self):
        self.heap = []
    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        self._swap(0, len(self.heap) - 1)
        max_val = self.heap.pop()
        self._heapify_down(0)
        return max_val
    def _heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[parent] < self.heap[index]:
            self._swap(parent, index)
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self._swap(index, largest)
            self._heapify_down(largest)
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    def __str__(self):
        return str(self.heap)





heap = Maxheap()
numbers = [5, 3, 8, 1, 2, 7, 9, 4, 6]
print("Inserting numbers:", numbers)
for num in numbers:
    heap.insert(num)
    print(f"After inserting {num}: {heap}")
print("\nPopping elements in descending order:")
while heap.heap:
    print(heap.pop(), end=" ")
