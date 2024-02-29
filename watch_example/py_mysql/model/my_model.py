class UserDto:
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier


class UserMovieDto:
    def __init__(self, user_identifier, movie_name, image_url, star):
        self.user_identifier = user_identifier
        self.movie_name = movie_name
        self.image_url = image_url
        self.star = star
