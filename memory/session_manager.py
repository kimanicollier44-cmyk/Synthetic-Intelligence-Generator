import json
import os


class SessionManager:

    def __init__(
        self,
        path="data/sessions"
    ):

        self.path = path

        os.makedirs(
            self.path,
            exist_ok=True
        )

    def save_session(
        self,
        session_id,
        history
    ):

        file_path = os.path.join(
            self.path,
            f"{session_id}.json"
        )

        with open(
            file_path,
            "w"
        ) as f:

            json.dump(
                history,
                f,
                indent=2
            )

    def load_session(
        self,
        session_id
    ):

        file_path = os.path.join(
            self.path,
            f"{session_id}.json"
        )

        if not os.path.exists(
            file_path
        ):
            return []

        with open(
            file_path,
            "r"
        ) as f:

            return json.load(f)
          
