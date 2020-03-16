from data_structures.linked_list import LinkedList, Node
from data_structures.hashtable import HashTable

class ChainedHashTable(HashTable):

    def __init__(self, size):

        super().__init__(size)
        self.table = [LinkedList()] * size

    def insert(self, value):

        node = Node(value)
        self.table[self.hash_func(value)].insert(node)

    def remove(self, value):

        return self.table[self.hash_func(value)].remove(value)

    def search(self, value):

        return self.table[self.hash_func(value)].search(value)


class ChainedHashDivisionTable(ChainedHashTable):

    def __init__(self, size):

        super().__init__(size)


class ChainedHashMultiplicationTable(ChainedHashTable):

    def __init__(self, size):

        super().__init__(size)

    def hash_func(self, value):

        return int((self.size - 1) * ((value * 0.618) - int(value * 0.618)))
