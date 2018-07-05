class Movies:
    def __init__(self, color, director_name, num_critic_for_reviews,
                 duration, director_facebook_likes, actor_3_facebook_likes,
                 actor_2_name, actor_1_facebook_likes, gross, genres, actor_1_name,
                 movie_title, num_voted_users, cast_total_facebook_likes, actor_3_name,
                 facenumber_in_poster, plot_keywords,movie_imdb_link,num_user_for_reviews,
                 language,country,content_rating,budget,title_year,actor_2_facebook_likes,
                 imdb_score,aspect_ratio, movie_facebook_likes):
        self.color = color
        self.director_name = director_name
        self.num_critic_for_reviews = num_critic_for_reviews
        self.duration = duration
        self.director_facebook_likes = director_facebook_likes
        self.actor_3_facebook_likes = actor_3_facebook_likes
        self.actor_2_name = actor_2_name
        self.actor_1_facebook_likes = actor_1_facebook_likes
        self.gross = gross
        self.genres = genres
        self.actor_1_name = actor_1_name
        self.movie_title = movie_title
        self.num_voted_users = num_voted_users
        self.cast_total_facebook_likes = cast_total_facebook_likes
        self.actor_3_name = actor_3_name
        self.facenumber_in_poster = facenumber_in_poster
        self.plot_keywords = plot_keywords
        self.movie_imdb_link = movie_imdb_link
        self.num_user_for_reviews = num_user_for_reviews
        self.language = language
        self.country = country
        self.content_rating = content_rating
        self.budget = budget
        self.year = title_year
        self.actor_2_facebook_likes = actor_2_facebook_likes
        self.imdb_score = imdb_score
        self.aspect_ratio = aspect_ratio
        self.movie_facebook_likes = movie_facebook_likes

    @staticmethod
    def create_from_dict(lookup):

        return Movies(
            lookup['color'],
            lookup['director_name'],
            lookup['num_critic_for_reviews'],
            lookup['duration'],
            lookup['director_facebook_likes'],
            lookup['actor_3_facebook_likes'],
            lookup['actor_2_name'],
            lookup['actor_1_facebook_likes'],
            lookup['gross'],
            lookup['genres'],
            lookup['actor_1_name'],
            lookup['movie_title'],
            lookup['num_voted_users'],
            lookup['cast_total_facebook_likes'],
            lookup['actor_3_name'],
            lookup['facenumber_in_poster'],
            lookup['plot_keywords'],
            lookup['movie_imdb_link'],
            lookup['num_user_for_reviews'],
            lookup['language'],
            lookup['country'],
            lookup['content_rating'],
            lookup['budget'],
            lookup['title_year'],
            lookup['actor_2_facebook_likes'],
            float(lookup['imdb_score']),
            lookup['aspect_ratio'],
            lookup['movie_facebook_likes'],
        )
