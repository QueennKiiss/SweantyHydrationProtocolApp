"""
Module for database management

"""
import logging
from datetime import datetime
from dataclasses import dataclass
import dropbox

from credentials import DROPBOX_TOKEN

logging.basicConfig(level=logging.DEBUG)


@dataclass()
class DropboxDBManager:
    """ Manager for dropbox database"""
    # Connect with business dropbox account
    dbx = dropbox.Dropbox(DROPBOX_TOKEN)

    def get_user_account(self) -> None:
        """List current user account"""
        logging.info("Getting current user account")
        try:
            print(self.dbx.users_get_current_account())
        except Exception as excp:
            logging.error(f" Exception occurs: {excp}")

    def get_folder_files(self, folder_name_path: str = "") -> None:
        """For listing the files in the specified folder
        arg:
            folder_name_path: The remote folder where to find files.
            (As default: empty string redirects to remote root folder)
        """
        logging.info(f"Listing files within the folder {folder_name_path}")
        for entry in self.dbx.files_list_folder(folder_name_path).entries:
            print(f"item: {entry.name}")

    def download_file_content(self, file_name_path: str) -> None:
        """Download indicated file"""
        logging.info(f"Downloading the file {file_name_path}")
        self.dbx.files_download(file_name_path)
        metadata, downloaded_file = self.dbx.files_download(file_name_path)
        print(f"META: {metadata}")
        print(f"FILE: {downloaded_file}")
        print(f"CONTENT: {downloaded_file.content}")
        return downloaded_file.content

    def download_file(self, remote_file_name_path: str, local_file_name_path: str) -> None:
        """Download indicated file"""
        logging.info(
            f"Downloading the file {remote_file_name_path} into {local_file_name_path}"
            )
        file_metadata = self.dbx.files_download_to_file(local_file_name_path, remote_file_name_path)
        # self.dbx.files_download_to_file('/database/users.txt', "/database/users.txt")
        print(f"META: {file_metadata}")

    def upload_file(self, data: str, file_name_path: str, file_mode: str = 'add'):
        """Upload the indicated file"""
        modes = {
            'add': dropbox.dropbox_client.files.WriteMode.add,
            'overwrite': dropbox.dropbox_client.files.WriteMode.overwrite,
            }
        mode = modes.get(file_mode)
        data_bytes = bytes(data, 'utf-8')
        logging.info(f"Updating the file {file_name_path}")
        # self.dbx.files_upload(data, file_path_name)
        self.dbx.files_upload(
            data_bytes, file_name_path, mode,
            client_modified=datetime.now(),
            mute=True
            )

    def get_file_metadata(self, file_name_path: str) -> None:
        """Get metadata info from indicated file"""
        logging.info(f"Getting the metadata of the file {file_name_path}")
        print(self.dbx.files_get_metadata(file_name_path).server_modified)


if __name__ == '__main__':
    logging.info("LOGGING Connecting to Dropbox database")
    dbx_manager = DropboxDBManager()
    # dbx_manager.get_user_account()
    # dbx_manager.get_folder_files()
    dbx_manager.get_folder_files("/database")
    # dbx_manager.get_file_metadata("/database/users.txt")
    dbx_manager.download_file_content("/database/users.txt")
