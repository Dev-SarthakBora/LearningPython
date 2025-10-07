# tuples.py

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.queue.append(item)

    def dequeue(self):
        """Remove and return the first item of the queue."""
        if not self.is_empty():
            return self.queue.popleft()
        return "Queue is empty"

    def peek(self):
        """Return the first item without removing it."""
        if not self.is_empty():
            return self.queue[0]
        return "Queue is empty"

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.queue)


# Example Usage
q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
print(q.dequeue())  # Output: A
print(q.peek())     # Output: B
print(q.size())     # Output: 2
