


class HashTable:

    def __init__(self, size):

        self.size = size
        self.table = [None] * size

    def hash_func(self, value):

        return value % (self.size - 1)

    def insert(self, value):

        self.table[self.hash_func(value)] = value

    def remove(self, value):

        self.table[self.hash_func(value)] = None

    def search(self, value):

        return self.table[self.hash_func(value)]


