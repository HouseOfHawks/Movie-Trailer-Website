import webbrowser

class Video():
    """Class for all videos, including TV Shows, Movies and Mini-Series"""
    
    def __init__(self, video_title, storyline, poster_image_url, trailer_youtube_url):
        self.title = video_title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class Movie(Video):
    """Class for full-length movie"""

    def __init__(self, video_title, rating, storyline, poster_image_url, trailer_youtube_url, run_time):
        VALID_RATINGS = ["G", "PG", "PG-13", "R"]
        Video.__init__(self, video_title, storyline, poster_image_url, trailer_youtube_url)
        self.rating = VALID_RATINGS[rating]
        self.run_time = run_time
        
class TvShow(Video):
    """Class for TV Series"""

    def __init__(self, video_title, rating, storyline, poster_image_url, trailer_youtube_url, seasons, network_img_url):
        VALID_RATINGS = ["Y", "Y7", "G", "PG", "14", "MA"]
        Video.__init__(self, video_title, storyline, poster_image_url, trailer_youtube_url)
        self.rating = "TV-" + VALID_RATINGS[rating]
        self.seasons = seasons
        self.network_img_url = network_img_url
