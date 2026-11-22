from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build


class GoogleDriveClient:

    SCOPES = [
        "https://www.googleapis.com/auth/drive"
    ]

    def __init__(
        self,
        credentials_file
    ):

        creds = Credentials.from_service_account_file(
            credentials_file,
            scopes=self.SCOPES
        )

        self.service = build(
            "drive",
            "v3",
            credentials=creds
        )

    def list_files(self):

        response = self.service.files().list(
            pageSize=100,
            fields="files(id,name)"
        ).execute()

        return response.get(
            "files",
            []
        )
      
