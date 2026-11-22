from googleapiclient.discovery import build


class CalendarConnector:

    def __init__(
        self,
        credentials
    ):

        self.service = build(
            "calendar",
            "v3",
            credentials=credentials
        )

    def upcoming_events(
        self,
        max_results=10
    ):

        events = (
            self.service.events()
            .list(
                calendarId="primary",
                maxResults=max_results,
                singleEvents=True,
                orderBy="startTime"
            )
            .execute()
        )

        return events.get(
            "items",
            []
        )
      
