from data_structures.queue import Queue
from data_structures.stack import Stack


class Deque(Queue):

    def __init__(self, size):

        super().__init__(size)

    def __repr__(self):

        return super().__repr__()

    def push_front(self, value):

        stack = Stack(self.size)

        while not self.is_empty():
            stack.push(self.dequeue())

        self.enqueue(value)

        while not stack.is_empty():
            self.enqueue(stack.pop())

    def remove_back(self):

        if not self.is_empty():
            self.tail = self.tail - 1
            value = self.queue[self.tail]
            self.queue[self.tail] = None
            
            return value

        return "The queue is empty."