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


if __name__ == "__main__":
    d = Deque(3)
    d.enqueue(3)
    d.push_front(3)
    print(d)
