import math

class DataStructuresVisualization:

    @staticmethod
    def queue(queue):

        queue_visualization = ""
        for i in range(queue.size):
            if i != queue.start:
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