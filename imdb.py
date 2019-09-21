

class IMBDMovieRatings:
    def __init__(self, basics, ratings):
        self.basics = basics
        self.ratings = ratings
        self.sorted_data = []
        self._process()

    def _process(self):
        self._match_with_ratings()
        self._sort_by_avarante_rating()

    def _match_with_ratings(self):
        for tconst, basic in self.basics.items():
            rating = self.ratings.get(tconst)
            if rating:
                basic['rating'] = float(rating['averageRating'])
            else:
                basic['rating'] = 0.0

    def _sort_by_avarante_rating(self):
        self.sorted_data = sorted(self.basics.items(), key=lambda x: x[1]['rating'], reverse=True)

    def search(self, word):
        def match_by_word(item, word):
            title = item[1]['primaryTitle']
            if word in title:
                return word

        return list(filter(lambda x: match_by_word(x, word), self.sorted_data))
