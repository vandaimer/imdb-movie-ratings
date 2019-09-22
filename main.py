from tabulate import tabulate
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
@click.option('-n', '--number-results', default=100, type=int, help='Number of results')
def main(load_data, search_word, number_results):
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
    movies = imdb.search(search_word)

    logger.info(f'Is going to show you the first {number_results} first result...')
    headers = ('Title', 'Rating')
    print(tabulate(list(map(lambda x: [x[1]['primaryTitle'], x[1]['rating']], movies[:number_results])), headers=headers))


if __name__ == '__main__':
    main()
