"""Why modules need docstring?"""


class Movie(object):
    """A model that represents movies"""
    def __init__(self, title, image_url, trailer_url):

        self.title = title
        self.poster_image_url = image_url
        self.trailer_youtube_url = trailer_url
