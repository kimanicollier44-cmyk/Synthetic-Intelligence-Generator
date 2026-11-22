from queue import Queue

class TaskQueue:

    def __init__(self):
        self.queue = Queue()

    def add_task(self, task):

        self.queue.put(task)

    def get_task(self):

        if self.queue.empty():
            return None

        return self.queue.get()

    def size(self):
        return self.queue.qsize()
      
