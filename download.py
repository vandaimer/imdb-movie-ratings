import gzip
import os
import requests
import shutil


class DownloadIMDBDatabase:
    BASE_URL = os.getenv('IMDB_BASE_URL', 'https://datasets.imdbws.com')

    def download(self, file_name):
        file_url = f'{self.BASE_URL}/{file_name}'
        file_path = file_name

        with requests.get(file_url, stream=True) as req:
            with open(file_path, 'wb') as file:
                shutil.copyfileobj(req.raw, file)

        return self._extract(file_path)

    def _extract(self, file_path):
        new_file_path = file_path.replace('.gz', '')

        with gzip.open(file_path, 'rb') as old_file:
            with open(new_file_path, 'wb') as new_file:
                shutil.copyfileobj(old_file, new_file)
