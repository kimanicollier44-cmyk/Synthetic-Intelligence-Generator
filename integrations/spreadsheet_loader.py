import pandas as pd


class SpreadsheetLoader:

    def load(
        self,
        file_path
    ):

        workbook = pd.read_excel(
            file_path,
            sheet_name=None,
            engine="openpyxl"
        )

        output = []

        for name, sheet in workbook.items():

            output.append(
                f"Sheet: {name}"
            )

            output.append(
                sheet.to_string()
            )

        return "\n".join(
            output
        )
      
