from pypdf import PdfReader


class PDFLoader:

    def load(
        self,
        file_path
    ):

        reader = PdfReader(
            file_path
        )

        content = []

        for page in reader.pages:

            text = (
                page.extract_text()
                or ""
            )

            content.append(text)

        return "\n".join(
            content
        )
      
