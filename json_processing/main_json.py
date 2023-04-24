# -*- coding: utf-8 -*-
from json_processing.json_utils import merge

movies_paths = ["movie\\movies_json","movie_rotten\\movies_json"]
users_paths = ["user\\users_json","user_rotten\\users_json" ]
reviews_paths = ["review\\reviews_json", "review\\reviews_json"]

# Para movies
merge(movies_paths,"all_movies.json","name",True)


# Para users
# merge(users_paths,"all_users.json","name",True)


# Para reviews
# merge(reviews_paths,"all_reviews.json","name")
