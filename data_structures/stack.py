from utils.data_structures_visualization import DataStructuresVisualization

class Stack:

    """
    This class implements the Abstract Data Type (TAD'S) stack, with it's main operations.
    ps: Since the list in Python is dynamic, it is necessary to enter the size to limit the stack.

    Params
    ----------
    size : int

    Methods
    -------
    push(value)
        Insert an element into the stack.

    pop()
        Removes the element from the top of the stack.

    is_empty()
        Checks if the stack is empty.

    is_full()
        Checks if the stack is full.
    """

    def __init__(self, size):
        
        self.size = size
        self.stack = [None] * size
        self.top = 0

    def __repr__(self):

        return "Stack:\n{0}".format(DataStructuresVisualization.stack(self))

    def is_empty(self):

        if self.top == 0:
            return True
        else:
            return False

    def is_full(self):

        if self.size == self.top:
            return True
        else:
            return False

    def push(self, value):

        if self.is_full():
            return "The stack is full."
        else:
            self.stack[self.top] = value
            self.top = self.top + 1

    def pop(self):

        if self.is_empty():
            return "The stack is empty.."
        self.top = self.top - 1
        return self.stack[self.top]