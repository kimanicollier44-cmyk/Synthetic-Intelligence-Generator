from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials


class GmailConnector:

    def __init__(
        self,
        credentials: Credentials
    ):

        self.service = build(
            "gmail",
            "v1",
            credentials=credentials
        )

    def list_messages(
        self,
        max_results=20
    ):

        result = (
            self.service.users()
            .messages()
            .list(
                userId="me",
                maxResults=max_results
            )
            .execute()
        )

        return result.get(
            "messages",
            []
        )

    def get_message(
        self,
        message_id
    ):

        return (
            self.service.users()
            .messages()
            .get(
                userId="me",
                id=message_id
            )
            .execute()
        )
      
