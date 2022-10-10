from multiprocessing.sharedctypes import Value
from turtle import title
import pytest
import sys, os
sys.path.insert(1, os.getcwd())
from src.movieAnalyzer import pd, get_movies_interval, get_rating_popularity_stats, get_actor_movies_release_year_range, get_actor_median_rating, get_directors_median_reviews

class TestMovieAnalyzer:
    def test_getMovieInterval(self):
        assert pd.Series.equals(get_movies_interval(1992, 1993),pd.Series({5:"Schindler's List", 88:"Reservoir Dogs", 131:"Unforgiven",141:"Jurassic Park",177:"In the Name of the Father",205:"Groundhog Day"}, name="Title"))
        assert pd.Series.equals(get_movies_interval(2008,2009), pd.Series({2:"The Dark Knight",56:"WALL·E",75:"Inglourious Basterds", 84:"3 Idiots", 107:"Up", 156:"The Secret in Their Eyes",162:"Gran Torino"}, name="Title"))
        assert pd.Series.equals(get_movies_interval(2008,2008), pd.Series({2:"The Dark Knight", 56:"WALL·E",162:"Gran Torino"}, name="Title"))
    def test_getMovieInterval_MismatchInterval(self):
        with pytest.raises(ValueError):
            get_movies_interval(1992,1991)
    def test_getRatingPopularity(self):
        assert get_rating_popularity_stats('Popularity Index', 'mean') == '1091.92'
        assert get_rating_popularity_stats('Popularity Index', 'max') == '4940.00'
        assert get_rating_popularity_stats('Popularity Index', 'min') == '3.00'
        assert get_rating_popularity_stats('Popularity Index', 'count') == '207.00'
        assert get_rating_popularity_stats('Rating', 'count') == '207.00'
        assert get_rating_popularity_stats('Rating', 'max') == '9.30'
        assert get_rating_popularity_stats('Rating', 'min') == '8.10'
        assert get_rating_popularity_stats('Rating', 'median') == '8.30'
    def test_getRatingPopularity_InvalidIndex(self):
        assert get_rating_popularity_stats("Year of Release", 'mean') == "Invalid index or type"
        assert get_rating_popularity_stats("Rating", 'stddev') == "Invalid index or type"
    def test_getActorReleasesRange(self):
        assert pd.Series.equals(get_actor_movies_release_year_range('Leonardo DiCaprio', 2022, 2010), pd.Series({"Inception":2010,"Django Unchained":2012,"The Wolf of Wall Street":2013,"Shutter Island":2010}))
        assert pd.Series.equals(get_actor_movies_release_year_range('Morgan Freeman', 2000, 1990), pd.Series({"The Shawshank Redemption":1994,"Se7en":1995,"Unforgiven":1992}))
        assert pd.Series.equals(get_actor_movies_release_year_range("Barack Obama", 2077, 2002), pd.Series([], dtype="int64"))
    def test_getActorReleasesRange_MismatchInterval(self):
        with pytest.raises(ValueError):
            get_actor_movies_release_year_range("Snoop Dogg", 2000, 9000)
    def test_getActorReleasesRange_BadType(self):
        with pytest.raises(TypeError):
            get_actor_movies_release_year_range(125, 2010, 2002)
        with pytest.raises(TypeError):
            get_actor_movies_release_year_range("Leonardo DiCaprio", "2010", 2002)
        with pytest.raises(TypeError):
            get_actor_movies_release_year_range("Leonardo DiCaprio", 2010, "2002")
    def test_getActorMedian(self):
        assert get_actor_median_rating("Leonardo DiCaprio") == 8.3
        assert get_actor_median_rating("Morgan Freeman") == 8.4
        assert get_actor_median_rating("Margot Robbie") == 8.2
    def test_getActorMedian_ActorNotFound(self):
        assert get_actor_median_rating("Barack Obama") == None
    def test_getActorMedian_EmptyString(self):
        with pytest.raises(ValueError):
            get_actor_median_rating("")
    def test_getActorMedian_NonString(self):
        with pytest.raises(TypeError):
            get_actor_median_rating(123)
    def test_getDirectorMedian(self):
        data = get_directors_median_reviews()
        assert data["Aamir Khan"] == 0.190
        assert data["Akira Kurosawa"] == 0.124
        assert data["Alfred Hitchcock"] == 0.397
        assert data["Andrew Stanton"] == 1.050
        assert data["Anthony Russo"] == 1.050
        assert data["Tony Kaye"] == 1.100
        assert data["Victor Fleming"] == 0.353
        assert data["Wes Anderson"] == 0.790
        assert data["William Wyler"] == 0.237
        assert data["Wolfgang Petersen"] == 0.248
        assert len(data) == 128
        assert data.index.name == "Director"
        assert data.name == None
            