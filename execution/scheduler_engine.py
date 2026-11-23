import heapq
import time


class SchedulerEngine:

    def __init__(self):

        self.queue = []

    def schedule(
        self,
        timestamp,
        task
    ):

        heapq.heappush(
            self.queue,
            (timestamp, task)
        )

    def next_task(self):

        if not self.queue:
            return None

        timestamp, task = (
            self.queue[0]
        )

        if time.time() >= timestamp:

            heapq.heappop(
                self.queue
            )

            return task

        return None
