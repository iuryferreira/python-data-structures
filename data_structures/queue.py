from utils.data_structures_visualization import DataStructuresVisualization

class Queue:

    def __init__(self, size):

        self.queue = [None] * size
        self.size = size
        self.start = 0
        self.end = 0

    def __repr__(self):

        return "Queue: {0}".format(DataStructuresVisualization.queue(self))

    def is_full(self):

        next_index = 0 if self.end == self.size else self.end
        if self.queue[next_index] is not None:
            return True
        return False 

    def is_empty(self):

        next_index = 0 if self.start == self.size else self.start
        if self.queue[next_index] is not None:
            return True
        return False 

    def enqueue(self, value):

        if self.is_full():
            return "The queue is full."
        else:
            if self.end == self.size:
                self.end = 0
            self.queue[self.end] = value
            self.end = self.end + 1

    def dequeue(self):

        if self.is_empty():
            return "The queue is empty."
        else:
            if self.start == self.size:
                self.start = 0
            value = self.queue[self.start]
            self.queue[self.start] = None
            self.start = self.start + 1
            return value