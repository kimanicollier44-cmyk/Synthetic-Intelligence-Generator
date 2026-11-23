import time


class ReasoningProfiler:

    def profile(
        self,
        function,
        *args,
        **kwargs
    ):

        start = time.time()

        result = function(
            *args,
            **kwargs
        )

        elapsed = (
            time.time() - start
        )

        return {

            "result": result,

            "duration": elapsed
        }
      
