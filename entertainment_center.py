"""This module is responsible to render a movie list"""

import json
from media import Movie
from fresh_tomatoes import open_movies_page

def create_movies_from_json(json_file):
    """Transform a json file in a Movie instance"""
    movie_list = []
    for data in json.load(open(json_file)):
        movie = Movie(data["title"], data["image"], data["trailer"])
        movie_list.append(movie)
    return movie_list

MY_FAVORITE_MOVIES = create_movies_from_json("my_favorite_movies.json")
open_movies_page(MY_FAVORITE_MOVIES)
