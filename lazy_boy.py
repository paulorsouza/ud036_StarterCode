"""
This module is to easy to get information of the all star wars movies
and to try create some cool things with python
This code has a lot of chance to throw error, but it is just for fun,
I do not even know handle exception in python yet
"""

import sys
import json
import urllib
import urllib2


def search_movie(title):
    """Receive a title and search in themoviedb for movie infos"""
    img_url = "https://image.tmdb.org/t/p/w300_and_h450_bestv2/"
    query_args = {"page": "1", "query": title,
                  "api_key": "4db22fd9f7e134e2440cb372ae452a44",
                  "language": "en-US"}
    enconded_args = urllib.urlencode(query_args)
    url = "https://api.themoviedb.org/3/search/movie?" + enconded_args
    response = urllib2.urlopen(url)
    data = json.loads(response.read())
    first = data["results"][0]
    print first["title"]
    trailer = get_trailer(first["id"])

    return {
        "title": first["title"],
        "image": img_url + first["poster_path"],
        "trailer": trailer}


def get_trailer(movie_id):
    """
    Receive a movie id and search in themoviedb for videos about this movie,
    then filter that videos to find one trailer, if not find a trailer
    return clip of the sound of silence that is a baita musica (good song)
    """
    query_args = {"api_key": "4db22fd9f7e134e2440cb372ae452a44",
                  "language": "en-US"}
    enconded_args = urllib.urlencode(query_args)
    url = ("https://api.themoviedb.org/3/movie/"
           + str(movie_id) + "/videos?" + enconded_args)
    # enconded_url = urllib.urlencode(url)
    response = urllib2.urlopen(url)
    data = json.loads(response.read())
    for video in data["results"]:
        if(video["type"] == "Trailer" and video["site"] == "YouTube"):
            return "https://www.youtube.com/watch?v=" + video["key"]
    # The sound of silence ^^
    return "https://www.youtube.com/watch?v=u9Dg-g7t2l4"


def run():
    """Generate json with movies info"""
    data_list = []
    args = sys.argv
    del args[0]
    for arg in args:
        movie_data = search_movie(arg)
        data_list.append(movie_data)

    outfile = open("lazy_boy.json", "w")
    json.dump(data_list, outfile)
    outfile.close()


if __name__ == "__main__":
    run()
