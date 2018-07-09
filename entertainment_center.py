# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

theDarkKnight_info 	= {	"title"		:	"The Dark Knight",
						"storyline"	:	"Batman vs. Joker",
						"poster"	:	"https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
						"trailer"	:	"https://www.youtube.com/watch?v=EXeTwQWrcwY"}


star_wars_V_info	= {	"title"		:	"Star Wars: Episode V - The Empire Strikes Back", 
						"storyline" :	"The Galactic Empire, under the leadership of the villainous Darth Vader and the Emperor, is in pursuit of Luke Skywalker and the rest of the Rebel Alliance.", 
						"poster"	:	"https://upload.wikimedia.org/wikipedia/en/thumb/3/3c/SW_-_Empire_Strikes_Back.jpg/220px-SW_-_Empire_Strikes_Back.jpg", 
						"trailer"	:	"https://www.youtube.com/watch?v=xESiohGGP7g"}

avatar_info			= {	"title"		:	"Avatar",
						"storyline" :	"Blue people defend their home world from the human invaders",
						"poster"	:	"https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
						"trailer"	:	"https://www.youtube.com/watch?v=5PSNL1qE6VY&t=11s"}

interstellar_info	= {	"title"		:	"Interstellar",
						"storyline"	:	"A farmer goes through a black hole to save earth",
						"poster"	:	"https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
						"trailer"	:	"https://www.youtube.com/watch?v=0vxOhd4qlnA"}

oblivion_info		= {	"title"		:	"Oblivion",
						"storyline" :	"One member of Earth's 'Mop Up Crew' finds out things aren't what they seem",
						"poster"	:	"https://upload.wikimedia.org/wikipedia/en/2/2e/Oblivion2013Poster.jpg",
						"trailer"	:	"https://www.youtube.com/watch?v=IBVkUb_TWp8"}

infinity_war_info	= {	"title"		:	"Avengers: Infinity War",
						"storyline"	:	"The Avengers must try to stop Thanos from wiping out half the universe",
						"poster"	:	"https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",
						"trailer"	:	"https://www.youtube.com/watch?v=6ZfuNTqbHE8"}


avatar = media.Movie(avatar_info['title'], avatar_info['storyline'], avatar_info['poster'], avatar_info['trailer'])
theDarkKnight =	media.Movie(theDarkKnight_info['title'], theDarkKnight_info['storyline'], theDarkKnight_info['poster'], theDarkKnight_info['trailer'])
interstellar = media.Movie(interstellar_info['title'], interstellar_info['storyline'], interstellar_info['poster'], interstellar_info['trailer'])
star_wars_V = media.Movie(star_wars_V_info['title'], star_wars_V_info['storyline'], star_wars_V_info['poster'], star_wars_V_info['trailer'])
oblivion = media.Movie(oblivion_info['title'], oblivion_info['storyline'], oblivion_info['poster'], oblivion_info['trailer'])
infinitywar = media.Movie(infinity_war_info['title'], infinity_war_info['storyline'], infinity_war_info['poster'], infinity_war_info['trailer'])

movies = [avatar, theDarkKnight, interstellar, oblivion, infinitywar, star_wars_V]

fresh_tomatoes.open_movies_page(movies)
