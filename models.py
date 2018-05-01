class Movie:
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """
         Initiate an instance of a movie object
        :param title: String
        :param poster_image_url:String
        :param trailer_youtube_url: String
        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
