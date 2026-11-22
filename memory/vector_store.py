import json
import os


class VectorStore:

    def __init__(
        self,
        path="data/vectors.json"
    ):

        self.path = path

        if not os.path.exists(self.path):

            os.makedirs(
                os.path.dirname(path),
                exist_ok=True
            )

            with open(
                self.path,
                "w"
            ) as f:

                json.dump([], f)

    def save_memory(
        self,
        text
    ):

        memories = self.load_memories()

        memories.append({
            "text": text
        })

        with open(
            self.path,
            "w"
        ) as f:

            json.dump(
                memories,
                f,
                indent=2
            )

    def load_memories(self):

        with open(
            self.path,
            "r"
        ) as f:

            return json.load(f)
          
