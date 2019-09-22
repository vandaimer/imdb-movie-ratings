import random

from imdb import IMBDMovieRatings


class TestIMBDMovieRatings:
    def test_if_call_match_with_ratings_when_call_process(self, mocker):
        mocker.spy(IMBDMovieRatings, '_match_with_ratings')
        imdb = IMBDMovieRatings({}, {})
        imdb.process()
        expected = 1

        assert imdb._match_with_ratings.call_count == expected

    def test_if_call_sort_by_avarange_rating_when_call_process(self, mocker):
        mocker.spy(IMBDMovieRatings, '_sort_by_average_rating')
        imdb = IMBDMovieRatings({}, {})
        imdb.process()
        expected = 1

        assert imdb._sort_by_average_rating.call_count == expected

    def test_sort_by_average_rating(self, mocker):
        number_a = random.random()
        number_b = random.random()
        max_number = max(number_a, number_b)

        movies = {'421': {'rating': number_a}, '234': {'rating': number_b}}
        imdb = IMBDMovieRatings(movies, {})
        imdb._sort_by_average_rating()

        assert imdb.sorted_data[0][1]['rating'] == max_number

    def test_search_return_empty_list(self):
        word = 'my_search'
        imdb = IMBDMovieRatings({}, {})
        imdb.process()
        result = imdb.search(word)

        assert result == []

    def test_search_return_one_result(self, mocker):
        word = 'my_search'
        expected = [('123', {'primaryTitle': word})]
        imdb = IMBDMovieRatings({}, {})
        imdb.sorted_data = expected
        result = imdb.search(word)

        assert result == expected
