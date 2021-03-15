import pytest
# this makes sure we look also look at the parent directory to import from the playlist.py file
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from playlist_functions import *

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
	expected =['Sometimes','Mothership Connection (Star Child)','Another Brick in the Wall','Unfunky UFO','Mississippi Goddamn','Four Women','Killing Me Softly','Killing Me Softly']
	actual = get_playlist_titles(playlist)
	assert expected == actual

# Question 2: Write two test functions for search_by_artist
def test_by_artist(playlist):
	expected=['Bilal']
	actual=search_by_artist(playlist,'Bilal')
	assert expected == actual

def test_by_artist(playlist):
	expected=['Mississippi Goddamn','Four Women']
	actual=search_by_artist(playlist,'Nina Simone')
	assert expected == actual

# Question 3: Write two test functions for search_by_title
def test_by_titles(playlist):
	expected=[{'artist': 'Nina Simone', 'title': 'Four Women'}]
	actual=search_by_title(playlist,'Four Women')
	assert expected == actual

def test_by_titles(playlist):
	expected=[{'artist': 'Parliament', 'title': 'Unfunky UFO'}]
	actual= search_by_title(playlist,'Unfunky UFO')
	assert expected == actual