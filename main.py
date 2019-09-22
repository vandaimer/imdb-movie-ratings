import os
import click
import logging

from imdb import IMBDMovieRatings
from download import DownloadIMDBDatabase
from csv_reader import BasicsCSVReader, RatingsCSVReader

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)-5.5s]  %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger()

@click.command()
@click.option('-l', '--load-data', required=True, default=False, help='Load data from internet')
@click.option('-w', '--search-word', required=True, type=str, help='Word to search')
def main(load_data, search_word):
    TITLE_BASIC_FILE = os.getenv('TITLE_BASIC_FILE', 'title.basics.tsv')
    TITLE_RATINGS_FILE = os.getenv('TITLE_BASIC_FILE', 'title.ratings.tsv')
    BASE_URL = os.getenv('IMDB_BASE_URL', 'https://datasets.imdbws.com')

    download_manager = DownloadIMDBDatabase(BASE_URL)

    for file in [TITLE_BASIC_FILE, TITLE_RATINGS_FILE]:
        if not os.path.exists(file) or load_data:
            logger.info(f'Downloading {file} file...it can take some time, wait!')
            file = f'{file}.gz'
            download_manager.download(file)

    logger.info(f'Reading {TITLE_BASIC_FILE}.csv')
    basics = BasicsCSVReader(TITLE_BASIC_FILE)
    logger.info(f'Reading {TITLE_RATINGS_FILE}.csv')
    ratings = RatingsCSVReader(TITLE_RATINGS_FILE)

    logger.info('Initializing IMBDMovieRatings...')
    imdb = IMBDMovieRatings(basics.data, ratings.data)

    logger.info(f'Searching for {search_word} ...')


if __name__ == '__main__':
    main()
