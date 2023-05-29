"""
Module containing the database manager interface
"""

from abc import ABC, abstractmethod


class DBManager(ABC):
    """
    Abstract class as interface for the different database managers to implement
    """

    def __init__(self):
        pass

    @abstractmethod
    def get_all_content(self, table: str):
        """
        Get all the information stored in a database table of the database
        """

    @abstractmethod
    def get_filtered_content(self, table: str, **filters: dict):
        """
        Get specified information from the database using filters or indicators
        """
