from docx import Document


class DocxLoader:

    def load(
        self,
        file_path
    ):

        document = Document(
            file_path
        )

        text = []

        for paragraph in document.paragraphs:

            text.append(
                paragraph.text
            )

        return "\n".join(
            text
        )
      
