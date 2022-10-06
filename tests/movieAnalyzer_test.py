import pytest
import sys, os
sys.path.insert(1, os.getcwd())
from src.movieAnalyzer import pd, get_movies_interval, get_rating_popularity_stats, get_actor_movies_release_year_range, get_actor_median_rating, get_directors_median_reviews

class TestMovieAnalyzer:
    pass
