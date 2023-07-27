"""
Module containing the local database manager
"""

import pandas as pd


class LocalDBManager:
    """
    Acts as the manager for a local database based on local files
    """

    def __init__(self):
        pass

    def get_all_content(self, table: str) -> pd.DataFrame:
        """
        Get all the information stored in a database table of the database
        """
        content = pd.read_csv(table)
        print(content)
        print(content.dtypes)
        print(content.attrs)
        return content

    def get_filtered_content(self, table: str, **filters) -> list:
        """
        Get specified information from the database using filters or indicators
        """
        content = pd.read_csv(table)
        # print(content)
        # To filter by row or columns names
        # filtered_content = content.filter(like='BRAND', axis=1)
        if not filters:
            print("WARNING: No filter is specified. Returning the whole content ")
            filtered_content = content
            print(content)

        for key, value in filters.items():
            filtered_content = content[content[key] == value]
            print(f"FILTERED: {filtered_content}")
            # json_filtered_content = filtered_content.to_json(orient="records")
            # print(f"JSONed: {json_filtered_content}")

        suplement_list = []
        for suplement in filtered_content.iterrows():
            suplement_list.append(f"{suplement}")
        print(suplement_list)

        return suplement_list


if __name__ == '__main__':
    db_manager = LocalDBManager()
    # db_manager.get_all_content('suplement_db.csv')
    db_manager.get_filtered_content('suplement_db.csv', TYPE='Beguda')
    # db_manager.get_filtered_content('suplement_db.csv')
