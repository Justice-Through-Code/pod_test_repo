import pytest
# this makes sure we look also look at the parent directory to import from the playlist.py file
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from playlist_functions16 import *

@pytest.fixture
def playlist():
	return [
		{'artist': 'Bilal', 'title': 'Sometimes'},
		{'artist': 'Parliament', 'title': 'Mothership Connection (Star Child)'},
		{'artist': 'Pink Floyd', 'title': 'Another Brick in the Wall'},
		{'artist': 'Parliament', 'title': 'Unfunky UFO'},
		{'artist': 'Nina Simone', 'title': 'Mississippi Goddamn'},
		{'artist': 'Nina Simone', 'title': 'Four Women'},
		{'artist': 'Roberta Flack', 'title': 'Killing Me Softly'},
		{'artist': 'Fugees', 'title': 'Killing Me Softly'}
	]

# Question 1: Complete the test for get_playlist_titles function
def test_get_titles(playlist):
	expected = ["Sometimes", "Mothership Connection (Star Child)", "Another Brick in the Wall", "Unfunky UFO", "Mississippi Goddamn", "Four Women", "Killing me Softly", 'Killing Me Softly']
	actual = get_playlist_titles(playlist)
	assert actual == expected

# Question 2: Write two test functions for search_by_artist
def test_search_fugees(playlist):
	expected = ["Killing Me Softly"]
	actual = search_by_artist(playlist, "Fugees")
	assert actual == expected

def test_search_roberta(playlist):
	expected = ["Killing Me Softly"]
	actual = search_by_artist(playlist, "Roberta Flack")
	assert actual == expected

# Question 3: Write two test functions for search_by_title

def test_search_somtimes(playlist):
	expected = [
		{'artist': 'Bilal', 'title': 'Sometimes'}
		]
	actual = search_by_title(playlist, "Sometimes")
	assert actual == expected

def test_search_killing(playlist):
	expected = [
		{'artist': 'Roberta Flack', 'title': 'Killing Me Softly'},
		{'artist': 'Fugees', 'title': 'Killing Me Softly'}"
	]
	actual = search_by_title(playlist, "Killing Me Softly")
	assert actual == expected
