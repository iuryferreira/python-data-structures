from data_structures.utils.data_structures_visualization import DataStructuresVisualization


class Queue:

    """
    This class implements the Abstract Data Type (TAD'S) Queue, with it's main operations.
    ps: Since the list in Python is dynamic, it is necessary to enter the size to limit the queue.

    Params
    ----------
    size : int

    Methods
    -------
    enqueue(value)
        Insert an element into the queue.

    dequeue()
        Removes the element from the front of the queue.

    is_empty()
        Checks if the queue is empty.

    is_full()
        Checks if the queue is full.
    """

    def __init__(self, size):

        self.queue = [None] * size
        self.size = size
        self.head = 0
        self.tail = 0

    def __repr__(self):

        return "Queue: {0}".format(DataStructuresVisualization.queue(self))

    def is_full(self):

        next_index = 0 if self.tail == self.size else self.tail
        if self.queue[next_index] is not None:
            return True
        return False

    def is_empty(self):

        next_index = 0 if self.head == self.size else self.head
        if self.queue[next_index] is not None:
            return False
        self.head, self.tail = 0, 0
        return True

    def enqueue(self, value):

        if self.is_full():
            return "The queue is full."
        else:
            if self.tail == self.size:
                self.tail = 0
            self.queue[self.tail] = value
            self.tail = self.tail + 1

    def dequeue(self):

        if self.is_empty():
            return "The queue is empty."
        else:
            if self.head == self.size:
                self.head = 0
            value = self.queue[self.head]
            self.queue[self.head] = None
            self.head = self.head + 1
            return value
