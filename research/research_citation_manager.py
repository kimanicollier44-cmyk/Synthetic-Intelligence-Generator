class ResearchCitationManager:

    def __init__(self):

        self.sources = []

    def add_source(
        self,
        title,
        url
    ):

        self.sources.append({

            "title": title,

            "url": url
        })

    def bibliography(self):

        lines = []

        for item in self.sources:

            lines.append(

                f"{item['title']} "
                f"({item['url']})"
            )

        return lines
      
