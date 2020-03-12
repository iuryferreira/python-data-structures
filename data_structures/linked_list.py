from data_structures.utils.data_structures_visualization import DataStructuresVisualization


class Node:

    """
    This class implements the node used by the linked lists.
    """

    def __init__(self, value):

        self.value = value
        self.next = None


class LinkedList:

    """
    This class implements the Abstract Data Type (TAD'S) Linked List, with it's main operations.

    Methods
    -------
    search(value_searched)
        Searches for a node.

    search_previous(value_searched)
        Fetches the node previous to the one containing the searched value.

    insert()
        Insert a node.

    remove()
        Removes a node.
    """

    def __init__(self):

        self.head = None

    def __repr__(self):

        return "LinkedList: {0}".format(DataStructuresVisualization.linkedlist(self))

    def search(self, value_searched):

        node = self.head
        while node is not None and node.value != value_searched:
            node = node.next
        return node

    def search_previous(self, value_searched):
        node = self.head
        while node is not None and node.next.value != value_searched:
            node = node.next
        return node

    def insert(self, node):

        node.next = self.head
        self.head = node

    def remove(self, value):

        if value == self.head.value:
            self.head = self.head.next
        else:
            node_prev = self.search_previous(value)
            node_prev.next = node_prev.next.next
