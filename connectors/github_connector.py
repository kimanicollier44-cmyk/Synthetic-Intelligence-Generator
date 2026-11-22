import requests


class GitHubConnector:

    def __init__(
        self,
        token=None
    ):

        self.token = token

    def get_repository(
        self,
        owner,
        repo
    ):

        headers = {}

        if self.token:

            headers["Authorization"] = (
                f"Bearer {self.token}"
            )

        url = (
            f"https://api.github.com/"
            f"repos/{owner}/{repo}"
        )

        response = requests.get(
            url,
            headers=headers,
            timeout=30
        )

        response.raise_for_status()

        return response.json()
      
