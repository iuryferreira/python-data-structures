from data_structures.linked_list import LinkedList, Node
from data_structures.hashtable import HashTable


class ChainedHashTable(HashTable):

    """
        This class implements the Abstract Data Type (TAD'S) Hash Table, with it's main operations, using chaining collision treatment. 

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

        super().__init__(size)
        self.table = [LinkedList() for posicao in range(size)]

    def insert(self, value):

        node = Node(value)
        self.table[self.hash_func(value)].insert(node)

    def remove(self, value):

        return self.table[self.hash_func(value)].remove(value)

    def search(self, value):

        return self.table[self.hash_func(value)].search(value)


class ChainedHashDivisionTable(ChainedHashTable):

    """
        This class inherits from ChainedHashTable, and implements the hash function by division.
    """

    def __init__(self, size):

        super().__init__(size)


class ChainedHashMultiplicationTable(ChainedHashTable):

    """
        This class inherits from ChainedHashTable, and implements the hash function by multiplication.
    """

    def __init__(self, size):

        super().__init__(size)

    def hash_func(self, value):

        return int((self.size - 1) * ((value * 0.618) - int(value * 0.618)))
