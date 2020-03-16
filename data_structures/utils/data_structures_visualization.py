import math
from tabulate import tabulate


class DataStructuresVisualization:

    @staticmethod
    def queue(queue):

        queue_visualization = ""
        for i in range(queue.size):
            if i != queue.head:
                queue_visualization += " [   %s   ] " % queue.queue[i]
            else:
                queue_visualization += " [→  %s  ←] " % queue.queue[i]
        return queue_visualization

    @staticmethod
    def stack(stack):

        stack_visualization = ""
        for i in range((stack.size - 1), -1, -1):
            if i != stack.top:
                item_visualization = "[ %s ]\n" % stack.stack[i]
                stack_visualization += item_visualization.rjust(30, '_')
            else:
                item_visualization = "[→%s←]\n" % stack.stack[i]
                stack_visualization += item_visualization.rjust(30, '_')
        return stack_visualization

    @staticmethod
    def linkedlist(linkedlist):

        node = linkedlist.head
        linkedlist_visualization = ""
        while node is not None:
            if linkedlist_visualization == "":
                linkedlist_visualization = linkedlist_visualization + \
                    " HEAD[%d] " % node.value
            else:
                linkedlist_visualization = linkedlist_visualization + \
                    " -> [%d] " % node.value
            node = node.next
        linkedlist_visualization = linkedlist_visualization + " -> [None]"
        return linkedlist_visualization

    @staticmethod
    def doublylinkedlist(doublylinkedlist):
        node = doublylinkedlist.head
        doublylinkedlist_visualization = ""
        while node is not None:
            if doublylinkedlist_visualization == "":
                doublylinkedlist_visualization = doublylinkedlist_visualization + \
                    " HEAD[%d] " % node.value
            else:
                doublylinkedlist_visualization = doublylinkedlist_visualization + \
                    " ←→ [%d] " % node.value
            node = node.next
        doublylinkedlist_visualization = doublylinkedlist_visualization + \
            " → [None]"
        return doublylinkedlist_visualization

    @staticmethod
    def direct_address_table(table):

        table_visualization = []
        headers = ["Key", "Value"]
        for value in table:
            table_visualization.append([str(value), value])

        return tabulate(table_visualization, headers, tablefmt="fancy_grid")

    @staticmethod
    def hash_table(table):

        table_visualization = []
        headers = ["Key", "Value"]
        pos = 0
        for value in table:
            table_visualization.append([str(pos), value])
            pos += 1

        return tabulate(table_visualization, headers, tablefmt="fancy_grid")

    @staticmethod
    def open_address_hash_table(table):

        table_visualization = []
        headers = ["Key", "Value"]
        pos = 0
        for value in table:
            table_visualization.append([str(pos), value])
            pos += 1

        return tabulate(table_visualization, headers, tablefmt="fancy_grid")
