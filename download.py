import gzip
import os
import requests
import shutil


class DownloadIMDBDatabase:
    def __init__(self, base_url):
        self.base_url = base_url

    def download(self, file_name):
        file_url = f'{self.base_url}/{file_name}'
        file_path = file_name

        with requests.get(file_url, stream=True) as req:
            with open(file_path, 'wb') as file:
                shutil.copyfileobj(req.raw, file)

        self._extract(file_path)

    def _extract(self, file_path):
        new_file_path = file_path.replace('.gz', '')

        with gzip.open(file_path, 'rb') as old_file:
            with open(new_file_path, 'wb') as new_file:
                shutil.copyfileobj(old_file, new_file)
