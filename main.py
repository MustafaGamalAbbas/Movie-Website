import fresh_tomatoes as ft
from models import Movie

avengers_movie = Movie("Avengers",
                       "http://image.tmdb.org/t/p/w342/7WsyChQLEftFiDOVTGkv3hFpyyt.jpg",
                       "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

zootopia_movie = Movie("Zootopia",
                       "http://image.tmdb.org/t/p/w342/sM33SANp9z6rXW8Itn7NnG1GOEs.jpg",
                       "https://www.youtube.com/watch?v=jWM0ct-OLsM")

coco_movie = Movie("Coco",
                   "http://image.tmdb.org/t/p/w342/eKi8dIrr8voobbaGzDpe8w0PVbC.jpg",
                   "https://www.youtube.com/watch?v=Ga6RYejo6Hk")

rampage_movie = Movie("Rampage",
                      "http://image.tmdb.org/t/p/w342/30oXQKwibh0uANGMs0Sytw3uN22.jpg",
                      "https://www.youtube.com/watch?v=coOKvrsmQiI")

movies_list = [avengers_movie, zootopia_movie, coco_movie, rampage_movie]

ft.open_movies_page(movies_list)
