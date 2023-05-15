"""
Module for database management

"""
from datetime import datetime
from dataclasses import dataclass
import dropbox
from credentials import DROPBOX_TOKEN






@dataclass()
class DropboxDBManager:
    # Connect with business dropbox account
    dbx = dropbox.Dropbox(DROPBOX_TOKEN)

    def get_user_account(self) -> None:
        """List current user account"""
        self.dbx.users_get_current_account()

    def get_folder_files(self, folder_name_path: str) -> None:
        """For listing the files in the specified folder"""
        for entry in self.dbx.files_list_folder(folder_name_path).entries:
            print(entry.name)

    def download_file(self, file_name_path: str) -> None:
        """Download indicated file"""
        self.dbx.files_download(file_name_path)

    def upload_file(self, data: str, file_name_path: str, file_mode: str):
        """Upload the indicated file"""
        modes = {
            'add': dropbox.dropbox_client.files.WriteMode.add,
            'overwrite': dropbox.dropbox_client.files.WriteMode.overwrite,
            }
        mode = modes.get(file_mode)

        # self.dbx.files_upload(data, file_path_name)
        self.dbx.files_upload(
            data, file_name_path, mode,
            client_modified=datetime.now(),
            mute=True
            )

    def get_file_metadata(self, file_name_path: str) -> None:
        # Get metadata info from indicated file
        print(self.dbx.files_get_metadata(file_name_path).server_modified)
