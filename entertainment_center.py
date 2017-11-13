# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

#toy_story = media.Movie()

jaws = media.Movie("Jaws","http://www.horrordvds.com/reviews/a-m/jaws/jaws_fl.jpg","https://youtu.be/U1fu_sA7XhE")
avatar = media.Movie("Avatar","http://vignette3.wikia.nocookie.net/jamescameronsavatar/images/7/7d/Avatar_Poster_3.jpg","https://youtu.be/d1_JBMrrYw8")
star_wars = media.Movie("Star Wars","https://thumbs.gfycat.com/AnxiousUnevenFrog-small.gif","https://youtu.be/76ZEIEbjlEg")

movies = [avatar,jaws,star_wars]
fresh_tomatoes.open_movies_page(movies)
