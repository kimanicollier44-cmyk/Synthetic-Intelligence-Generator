import time


class CacheManager:

    def __init__(self):

        self.cache = {}

    def set(
        self,
        key,
        value,
        ttl=3600
    ):

        self.cache[key] = {

            "value": value,

            "expires":
            time.time() + ttl
        }

    def get(
        self,
        key
    ):

        item = self.cache.get(
            key
        )

        if not item:
            return None

        if time.time() > item[
            "expires"
        ]:

            del self.cache[key]

            return None

        return item["value"]

    def clear(self):

        self.cache.clear()
      
