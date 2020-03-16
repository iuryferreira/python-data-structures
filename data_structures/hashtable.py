from data_structures.utils.data_structures_visualization import DataStructuresVisualization

class HashTable:

    """
        This class implements the Abstract Data Type (TAD'S) Hash Table, with it's main operations.

        Methods
        -------
        hash_func(value)
            returns the position that the element is to be stored.

        search(value)
            Searches for a value.

        insert()
            Insert a value.

        remove()
            Removes a value.
        """

    def __init__(self, size):

        self.size = size
        self.table = [None] * size

    def __repr__(self):

        return "\nHash Table:\n{0}".format(DataStructuresVisualization.hash_table(self.table))

    def hash_func(self, value):

        return value % self.size

    def insert(self, value):

        self.table[self.hash_func(value)] = value

    def remove(self, value):

        self.table[self.hash_func(value)] = None

    def search(self, value):

        return self.table[self.hash_func(value)]


