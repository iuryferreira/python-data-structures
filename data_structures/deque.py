from data_structures.queue import Queue
from data_structures.stack import Stack


class Deque(Queue):

    """
    This class implements the Abstract Data Type (TAD'S) Queue, with it's main operations.

    ps: Since the list in Python is dynamic, it is necessary to enter the size to limit the queue.

    Params
    ----------
    size : int

    Methods
    -------
    enqueue(value)
        Insert an element into the deque.

    dequeue()
        Removes the element from the front of the deque.

    is_empty()
        Checks if the deque is empty.

    is_full()
        Checks if the deque is full.

    push_front(value)
        Inserts an element at the head.

    remove_back()
        Removes an element at the tail.


    """

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