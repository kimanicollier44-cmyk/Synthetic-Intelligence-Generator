import time
import logging


class Monitoring:

    def __init__(self):

        self.logger = logging.getLogger(
            "monitoring"
        )

    def track(
        self,
        operation,
        function,
        *args,
        **kwargs
    ):

        start = time.time()

        result = function(
            *args,
            **kwargs
        )

        duration = (
            time.time() - start
        )

        self.logger.info(
            f"{operation} "
            f"completed in "
            f"{duration:.2f}s"
        )

        return result
      
