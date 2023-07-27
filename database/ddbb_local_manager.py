"""
Module containing the local database manager
"""

import pandas as pd


class LocalDBManager:
    """
    Acts as the manager for a local database based on local files
    """

    def __init__(self):
        self.db_content = None

    def _format_db_entry(self, entry: pd.Series) -> str:
        suplement_type = entry['TYPE']
        suplement_brand = entry['BRAND']
        suplement_model = entry['MODEL']
        suplement_salt_content = entry['(mg_NaCl) per capsula/gel/1L']
        return f"{suplement_type} {suplement_brand} {suplement_model} -->  {suplement_salt_content} (mg_NaCl) per capsula/gel/1L"

    def read_data_from_db(self, table: str) -> pd.DataFrame:
        """
        Get all the information stored in a database table of the database
        """
        content = pd.read_csv(table)
        self.db_content = content
        return content

    def get_all_db_content(self) -> list:
        """
        Get specified information from the database using filters or indicators
        """
        supplement_list = []
        for _, supplement in self.db_content.iterrows():
            formatted_supplement = self._format_db_entry(supplement)
            supplement_list.append(f"{formatted_supplement}")

        return supplement_list

    def get_filtered_content(self, **filters) -> list:
        """
        Get specified information from the database using filters or indicators
        """
        content = self.db_content
        # To filter by row or columns names
        # filtered_content = content.filter(like='BRAND', axis=1)
        if not filters:
            print("WARNING: No filter is specified. Returning the whole content ")
            filtered_content = content
            print(content)

        for key, value in filters.items():
            filtered_content = content[content[key] == value]
            # print(f"FILTERED: {filtered_content}")
            # json_filtered_content = filtered_content.to_json(orient="records")
            # print(f"JSONed: {json_filtered_content}")

        supplement_list = []
        for _, supplement in filtered_content.iterrows():
            formatted_supplement = self._format_db_entry(supplement)
            supplement_list.append(f"{formatted_supplement}")

        return supplement_list
