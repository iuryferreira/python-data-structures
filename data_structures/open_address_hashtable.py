from data_structures.hashtable import HashTable
from data_structures.utils.data_structures_visualization import DataStructuresVisualization


class OpenAddressHashTable(HashTable):

    def __init__(self, size):

        super().__init__(size)

    def hash_func(self, value, sequence):

        return (super().hash_func(value) + (sequence - 2)) % (self.size)

    def __repr__(self):

        return "\nOpen Address HashTable:\n{0}".format(DataStructuresVisualization.open_address_hash_table(self.table))

    def insert(self, value):

        sequence = 0

        while sequence != self.size:

            position = self.hash_func(value, sequence)

            if self.table[position] is None:
                self.table[position] = value
                return position
            else:
                sequence += 1

        return "All fields have already been filled."

    def search(self, value):

        sequence = 0

        while sequence != self.size:

            position = self.hash_func(value, sequence)
            if self.table[position] == value:
                return position
            else:
                sequence += 1
        return None

    def remove(self, value):

        position = self.search(value)
        if position is None:
            return "All fields are empty."
        else:
            self.table[position] = None


class OpenAddressHashTableLinearProbing(OpenAddressHashTable):

    def __init__(self, size):

        super().__init__(size)


class OpenAddressHashTableQuadraticProbing(OpenAddressHashTable):

    def __init__(self, size, c1, c2):

        self.c1 = c1
        self.c2 = c2
        super().__init__(size)

    def hash_func(self, value, sequence):

        return (super().hash_func(value) - 1 + self.c1 *
         (sequence-1) + (self.c2 * (sequence-1)) ^ 2) % (self.size)