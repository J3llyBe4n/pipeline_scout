from datetime import datetime, timezone
import os, json

class json_management:

    def make_folders(self, folder_directory):
        date = datetime.now(timezone.utc).date()
        os.mkdir(f"{folder_directory}/{date}")

    def json_append(self, folder_directory, list):
        date = datetime.now(timezone.utc).date()
        file_name = f"{folder_directory}/{date}/{date}.json"
        for data in list:
            with open(f"{file_name}", "a") as file:
                json.dump(data, file)