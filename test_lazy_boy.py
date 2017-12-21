"""Lazy boy unit tests"""
import pytest
import vcr
import lazy_boy

def test_search_movie():
    "Should return correct movie"
    with vcr.use_cassette('fixtures/vcr_cassettes/star_wars.yaml'):
        movie = lazy_boy.search_movie("Star wars 1")
        assert movie["title"] == "Star Wars: Episode I - The Phantom Menace"
        assert movie["trailer"] == "https://www.youtube.com/watch?v=bD7bpG-zDJQ"

def test_search_invalid_movie():
    "I should treat this error, but Im not"
    with vcr.use_cassette('fixtures/vcr_cassettes/xqdle.yaml'):
        with pytest.raises(IndexError):
            lazy_boy.search_movie("Xquedele")
