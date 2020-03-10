class DataStructuresVisualization:
    @staticmethod
    def queue(queue):
        queue_visualization = ""
        for i in range(queue.size):
            if i != queue.start:
                queue_visualization += " [  %s  ] " % queue.queue[i]
            else:
                queue_visualization += " [→ %s ←] " % queue.queue[i]
        return queue_visualization
