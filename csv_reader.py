import csv
import os


class CSVReader:
    def __init__(self, file_path=None):
        if file_path is None:
            raise ValueError('The file path is required.')

        current_dir = os.getcwd()

        self.file_path = os.path.join(current_dir, file_path)
        self.data = []
        self.read_data()

    def read_data(self):
        try:
            with open(self.file_path, 'r') as file:
                reader = csv.reader(file)
                next(reader, None)
                for row in reader:
                    self.add_item(row)
        except (FileNotFoundError, IOError):
            print('File not found.')

    def add_item(self, item):
        raise NotImplementedError('This method needs be overwritten.')


class BasicsCSVReader(CSVReader):
    TITLE_TYPE = 'movie'

    def add_item(self, item):
        if item[1] == self.TITLE_TYPE:
            self.data.append({
                'tconst': item[0],
                'primaryTitle': item[2],
                'originalTitle': item[3],
            })


class RatingsCSVReader(CSVReader):
    def add_item(self, item):
        self.data.append({
            'tconst': item[0],
            'averageRating': item[1],
            'numVotes': item[2],
        })
