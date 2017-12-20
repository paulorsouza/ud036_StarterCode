from media import Movie
from fresh_tomatoes import open_movies_page

def create_my_favorite_movies():
    """Return a list of my favorite Movies"""
    return [
        Movie(
            "Star Wars: Episode IV - A New Hope",
            "https://images-na.ssl-images-amazon.com/images/M/MV5BNzVlY2MwMjktM2E4OS00Y2Y3LWE3ZjctYzhkZGM3YzA1ZWM2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SY1000_CR0,0,643,1000_AL_.jpg", # pylint: disable=C0301
            "https://www.youtube.com/watch?v=oVxcQQXXxGQ"
        ),
        Movie(
            "Star Wars: The Force Awakens",
            "https://images-na.ssl-images-amazon.com/images/M/MV5BOTAzODEzNDAzMl5BMl5BanBnXkFtZTgwMDU1MTgzNzE@._V1_SY1000_CR0,0,677,1000_AL_.jpg", # pylint: disable=C0301
            "https://www.youtube.com/watch?v=sGbxmsDFVnE"
        ),
        Movie(
            "Inception",
            "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg", # pylint: disable=C0301
            "https://www.youtube.com/watch?v=8hP9D6kZseM"
        )
    ]

open_movies_page(create_my_favorite_movies())
