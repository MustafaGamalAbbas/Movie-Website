import fresh_tomatoes as ft
from models import Movie

avengers_movie = Movie()
avengers_movie.movie_title = "Avengers"
avengers_movie.poster_image_url = "http://image.tmdb.org/t/p/w342/7WsyChQLEftFiDOVTGkv3hFpyyt.jpg"
avengers_movie.trailer_youtube_url = "https://www.youtube.com/watch?v=6ZfuNTqbHE8"

zootopia_movie = Movie()
zootopia_movie.movie_title = "Zootopia"
zootopia_movie.poster_image_url = "http://image.tmdb.org/t/p/w342/sM33SANp9z6rXW8Itn7NnG1GOEs.jpg"
zootopia_movie.trailer_youtube_url = "https://www.youtube.com/watch?v=jWM0ct-OLsM"

coco_movie = Movie()
coco_movie.movie_title = "Coco"
coco_movie.poster_image_url = "http://image.tmdb.org/t/p/w342/eKi8dIrr8voobbaGzDpe8w0PVbC.jpg"
coco_movie.trailer_youtube_url = "https://www.youtube.com/watch?v=Ga6RYejo6Hk"

rampage_moive = Movie()
rampage_moive.movie_title = "Rampage"
rampage_moive.poster_image_url = "http://image.tmdb.org/t/p/w342/30oXQKwibh0uANGMs0Sytw3uN22.jpg"
rampage_moive.trailer_youtube_url = "https://www.youtube.com/watch?v=coOKvrsmQiI"

movies = (avengers_movie, zootopia_movie, coco_movie, rampage_moive)
ft.open_movies_page(movies)
