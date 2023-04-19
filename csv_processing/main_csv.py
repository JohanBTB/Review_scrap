# -*- coding: utf-8 -*-

from csv_processing.csv_utils import transform_to_csv
import os


# user_path = os.path.join(os.getcwd(), "json_processing","json_files","all_users.json")
# movie_path = os.path.join(os.getcwd(), "json_processing","json_files","all_movies.json")
# review_path = os.path.join(os.getcwd(), "json_processing","json_files","all_reviews.json")

transform_to_csv(movie_path, "reviews.csv")