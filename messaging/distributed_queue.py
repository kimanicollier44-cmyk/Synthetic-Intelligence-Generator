from queue import Queue


class DistributedQueue:

    def __init__(self):

        self.channels = {}

    def channel(
        self,
        name
    ):

        if name not in self.channels:

            self.channels[name] = Queue()

        return self.channels[name]

    def push(
        self,
        channel,
        item
    ):

        self.channel(
            channel
        ).put(item)

    def pull(
        self,
        channel
    ):

        queue = self.channel(
            channel
        )

        if queue.empty():
            return None

        return queue.get()
      
