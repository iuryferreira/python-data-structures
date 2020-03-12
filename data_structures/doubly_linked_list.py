from data_structures.linked_list import Node, LinkedList
from data_structures.utils.data_structures_visualization import DataStructuresVisualization


class DoublyLinkedNode(Node):

    """
    This class implements the node used by the Doubly Linked Lists.
    """

    def __init__(self, value):

        self.previous = None
        super().__init__(value)


class DoublyLinkedList(LinkedList):

    """
    This class implements the Abstract Data Type (TAD'S) Doubly Linked List, with it's main operations.

    Methods
    -------
    search(value_searched)
        Searches for a node.

    insert(node)
        Insert a node.

    insert_before(node_after, new_node)
        inserts a node before another specified node.

    insert_after(node_previous, new_node)
        Insert a Node after another specified node.

    remove(value)
        Removes a node.
    """

    def __init__(self):

        super().__init__()

    def __repr__(self):

        return "DoublyLinkedList: {0}".format(DataStructuresVisualization.doublylinkedlist(self))

    def insert(self, node):

        node.next = self.head
        if node.next is not None:
            node.next.previous = node
        self.head = node

    def insert_before(self, node_after, new_node):

        if self.head == node_after:
            self.head = new_node
        new_node.next = node_after
        new_node.previous = node_after.previous
        node_after.previous = new_node

    def insert_after(self, node_previous, new_node):

        new_node.previous = node_previous
        new_node.next = node_previous.next
        node_previous.next = new_node

    def remove(self, value):

        node = self.search(value)

        if node == self.head:
            self.head = None
        else:
            node.previous.next = node.next
            if node.next is not None:
                node.next.previous = node.previous
            node.next = None
            node.previous = None
