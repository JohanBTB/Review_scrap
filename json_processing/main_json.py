# -*- coding: utf-8 -*-
from json_processing.json_utils import merge
import os

movies_path = os.path.join(os.getcwd(), "movie\\movies_json")
users_path = os.path.join(os.getcwd(), "user\\users_json")
reviews_path = os.path.join(os.getcwd(), "review\\reviews_json")

# Para movies
merge(movies_path,"all_movies.json","name",True)


# Para users
merge(users_path,"all_users.json","name",True)


# Para reviews
merge(reviews_path,"all_reviews.json","name")
