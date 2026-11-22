import time


class MemoryScheduler:

    def __init__(
        self,
        vector_store
    ):

        self.store = vector_store

    def cleanup(
        self,
        max_entries=10000
    ):

        memories = (
            self.store.load_memories()
        )

        if len(memories) <= max_entries:
            return

        memories = memories[
            -max_entries:
        ]

        self.store.save_all(
            memories
        )

    def run_cycle(self):

        while True:

            self.cleanup()

            time.sleep(3600)
          
