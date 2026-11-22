from pathlib import Path


class DocumentParser:

    def __init__(self):
        self.supported = {
            ".txt",
            ".md"
        }

    def parse(
        self,
        file_path
    ):

        extension = (
            Path(file_path)
            .suffix
            .lower()
        )

        if extension not in self.supported:
            raise ValueError(
                f"Unsupported type: {extension}"
            )

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()
          
