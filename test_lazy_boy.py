"""Lazy boy unit tests"""
import pytest
import lazy_boy

def test_search_movie():
    "Should return correct movie"
    movie = lazy_boy.search_movie("Star wars 1")
    assert movie["title"] == "Star Wars: Episode I - The Phantom Menace"
    assert movie["trailer"] == "https://www.youtube.com/watch?v=bD7bpG-zDJQ"

def test_search_invalid_movie():
    "I should treat this error, but Im not"
    with pytest.raises(IndexError):
        lazy_boy.search_movie("Xquedele")
