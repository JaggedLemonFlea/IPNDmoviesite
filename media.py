# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

import webbrowser

class Movie():
    # This class provides a way to store movie related information

    def __init__(self, movieTitle, movieStory, moviePoster, movieTrailer):
        # initialize instance of class Movie
        self.title = movieTitle
        self.storyline = movieStory
        self.poster_image_url = moviePoster
        self.trailer_youtube_url = movieTrailer

    def show_trailer(self):
    	# dispays the url passed in "self.trailer" in the default browser
    	webbrowser.open(self.trailer)
