import os


class DriveSync:

    def __init__(
        self,
        drive_client
    ):

        self.drive_client = drive_client

    def sync_metadata(
        self,
        output_path
    ):

        files = self.drive_client.list_files()

        os.makedirs(
            output_path,
            exist_ok=True
        )

        index_file = os.path.join(
            output_path,
            "drive_index.txt"
        )

        with open(
            index_file,
            "w",
            encoding="utf-8"
        ) as f:

            for item in files:

                line = (
                    f"{item['id']} | "
                    f"{item['name']}\n"
                )

                f.write(line)

        return index_file
      
